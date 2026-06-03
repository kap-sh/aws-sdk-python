"""Generated from Smithy shape ``com.amazonaws.kms#XksKeyConfigurationType``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.xks_key_id_type


class XksKeyConfigurationType(TypedDict):
    id: NotRequired["awd_sdk_kms.types.xks_key_id_type.XksKeyIdType"]
    """<p>The ID of the external key in its external key manager. This is the ID that the external key store proxy uses to identify the external key.</p>"""
