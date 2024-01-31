# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmbedCreateParams"]


class EmbedCreateParams(TypedDict, total=False):
    texts: Required[List[str]]
    """An array of strings for the model to embed.

    Maximum number of texts per call is `96`. We recommend reducing the length of
    each text to be under `512` tokens for optimal quality.
    """

    model: str
    """The identifier of the model.

    Smaller "light" models are faster, while larger models will perform better.
    [Custom models](/docs/training-custom-models) can also be supplied with their
    full ID.

    Available models and corresponding embedding dimensions:

    - `embed-english-v2.0` (default) 4096
    - `embed-english-light-v2.0` 1024
    - `embed-multilingual-v2.0` 768
    """

    truncate: Literal["NONE", "START", "END"]
    """
    One of `NONE|START|END` to specify how the API will handle inputs longer than
    the maximum token length.

    Passing `START` will discard the start of the input. `END` will discard the end
    of the input. In both cases, input is discarded until the remaining input is
    exactly the maximum input token length for the model.

    If `NONE` is selected, when the input exceeds the maximum input token length an
    error will be returned.
    """
