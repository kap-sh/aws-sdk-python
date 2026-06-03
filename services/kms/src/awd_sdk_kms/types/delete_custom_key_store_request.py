"""Generated from Smithy shape ``com.amazonaws.kms#DeleteCustomKeyStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import awd_sdk_kms.types.custom_key_store_id_type


class DeleteCustomKeyStoreRequest(TypedDict):
    custom_key_store_id: (
        "awd_sdk_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    )
    """<p>Enter the ID of the custom key store you want to delete. To find the ID of a custom key store, use the <a>DescribeCustomKeyStores</a> operation.</p>"""
