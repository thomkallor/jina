__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import numpy as np

from .. import BaseNumericEncoder
from ...decorators import batching


class TSNEEncoder(BaseNumericEncoder):
    """
    :class:`TSNEEncoder` encodes data from an ndarray in size `B x T` into an ndarray in size `B x D`.
    https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
    """

    def __init__(self,
                 output_dim: int,
                 random_state: int,
                 *args,
                 **kwargs):
        """
        :param output_dim: the output size.
        """
        super().__init__(*args, **kwargs)
        self.output_dim = output_dim
        self.random_state = random_state

    def post_init(self):
        from sklearn.manifold import TSNE
        self.model = TSNE(n_components=self.output_dim, random_state=self.random_state)

    @batching
    def encode(self, data: 'np.ndarray', *args, **kwargs) -> 'np.ndarray':
        """
        :param data: a `B x T` numpy ``ndarray``, `B` is the size of the batch
        :return: a `B x D` numpy ``ndarray``
        """
        return self.model.fit_transform(data)