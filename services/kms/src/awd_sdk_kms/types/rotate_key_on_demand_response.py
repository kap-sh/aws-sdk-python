"""Generated from Smithy shape ``com.amazonaws.kms#RotateKeyOnDemandResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.key_id_type


class RotateKeyOnDemandResponse(TypedDict):
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>Identifies the symmetric encryption KMS key that you initiated on-demand rotation on.</p>"""
