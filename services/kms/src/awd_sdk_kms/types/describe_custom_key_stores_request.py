"""Generated from Smithy shape ``com.amazonaws.kms#DescribeCustomKeyStoresRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.custom_key_store_id_type
    import awd_sdk_kms.types.custom_key_store_name_type
    import awd_sdk_kms.types.limit_type
    import awd_sdk_kms.types.marker_type


class DescribeCustomKeyStoresRequest(TypedDict):
    custom_key_store_id: NotRequired[
        "awd_sdk_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    ]
    """<p>Gets only information about the specified custom key store. Enter the key store ID.</p> <p>By default, this operation gets information about all custom key stores in the account and Region. To limit the output to a particular custom key store, provide either the <code>CustomKeyStoreId</code> or <code>CustomKeyStoreName</code> parameter, but not both.</p>"""
    custom_key_store_name: NotRequired[
        "awd_sdk_kms.types.custom_key_store_name_type.CustomKeyStoreNameType"
    ]
    """<p>Gets only information about the specified custom key store. Enter the friendly name of the custom key store.</p> <p>By default, this operation gets information about all custom key stores in the account and Region. To limit the output to a particular custom key store, provide either the <code>CustomKeyStoreId</code> or <code>CustomKeyStoreName</code> parameter, but not both.</p>"""
    limit: NotRequired["awd_sdk_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p>"""
    marker: NotRequired["awd_sdk_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""
