"""Generated from Smithy shape ``com.amazonaws.kms#CreateCustomKeyStoreResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.custom_key_store_id_type


class CreateCustomKeyStoreResponse(TypedDict):
    custom_key_store_id: NotRequired[
        "awd_sdk_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    ]
    """<p>A unique identifier for the new custom key store.</p>"""
