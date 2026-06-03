"""Generated from Smithy shape ``com.amazonaws.kms#ConnectCustomKeyStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.custom_key_store_id_type


class ConnectCustomKeyStoreRequest(TypedDict):
    custom_key_store_id: (
        "aws_sdk_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    )
    """<p>Enter the key store ID of the custom key store that you want to connect. To find the ID of a custom key store, use the <a>DescribeCustomKeyStores</a> operation.</p>"""
