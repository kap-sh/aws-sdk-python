"""Generated from Smithy shape ``com.amazonaws.kms#DescribeCustomKeyStoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.custom_key_store_id_type
    import capo_kms.types.custom_key_store_name_type
    import capo_kms.types.limit_type
    import capo_kms.types.marker_type


class DescribeCustomKeyStoresRequest(TypedDict, closed=True):
    custom_key_store_id: NotRequired[
        "capo_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    ]
    """<p>Gets only information about the specified custom key store. Enter the key store ID.</p> <p>By default, this operation gets information about all custom key stores in the account and Region. To limit the output to a particular custom key store, provide either the <code>CustomKeyStoreId</code> or <code>CustomKeyStoreName</code> parameter, but not both.</p>"""
    custom_key_store_name: NotRequired[
        "capo_kms.types.custom_key_store_name_type.CustomKeyStoreNameType"
    ]
    """<p>Gets only information about the specified custom key store. Enter the friendly name of the custom key store.</p> <p>By default, this operation gets information about all custom key stores in the account and Region. To limit the output to a particular custom key store, provide either the <code>CustomKeyStoreId</code> or <code>CustomKeyStoreName</code> parameter, but not both.</p>"""
    limit: NotRequired["capo_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p>"""
    marker: NotRequired["capo_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomKeyStoresRequest) -> dict:
    out: dict = {}
    if "custom_key_store_id" in value:
        out["CustomKeyStoreId"] = value["custom_key_store_id"]
    if "custom_key_store_name" in value:
        out["CustomKeyStoreName"] = value["custom_key_store_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomKeyStoresRequest:
    out: DescribeCustomKeyStoresRequest = {}  # type: ignore[typeddict-item]
    if "CustomKeyStoreId" in data:
        out["custom_key_store_id"] = data["CustomKeyStoreId"]
    if "CustomKeyStoreName" in data:
        out["custom_key_store_name"] = data["CustomKeyStoreName"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
