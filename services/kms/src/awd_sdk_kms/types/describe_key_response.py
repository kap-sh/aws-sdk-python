"""Generated from Smithy shape ``com.amazonaws.kms#DescribeKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.key_metadata


class DescribeKeyResponse(TypedDict):
    key_metadata: NotRequired["awd_sdk_kms.types.key_metadata.KeyMetadata"]
    """<p>Metadata associated with the key.</p>"""
