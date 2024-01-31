# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["DetokenizeCreateResponse", "Meta", "MetaAPIVersion"]


class MetaAPIVersion(BaseModel):
    version: str

    is_deprecated: Optional[bool] = None

    is_experimental: Optional[bool] = None


class Meta(BaseModel):
    api_version: Optional[List[MetaAPIVersion]] = None

    warnings: Optional[List[str]] = None


class DetokenizeCreateResponse(BaseModel):
    text: str
    """A string representing the list of tokens."""

    meta: Optional[List[Meta]] = None
