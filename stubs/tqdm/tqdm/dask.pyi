from _typeshed import Incomplete

class TqdmCallback(Incomplete):  # base class is dask.callbacks.Callback
    tqdm_class: Incomplete
    def __init__(
        self, start: Incomplete | None = ..., pretask: Incomplete | None = ..., tqdm_class=..., **tqdm_kwargs
    ) -> None: ...
    def display(self) -> None: ...
