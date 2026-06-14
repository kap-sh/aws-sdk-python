"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListTapePoolsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.pool_ar_ns
    import aws_sdk_storage_gateway.types.positive_int_object


class ListTapePoolsInput(TypedDict):
    pool_ar_ns: NotRequired["aws_sdk_storage_gateway.types.pool_ar_ns.PoolARNs"]
    """<p>The Amazon Resource Name (ARN) of each of the custom tape pools you want to list. If you don't specify a custom tape pool ARN, the response lists all custom tape pools. </p>"""
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>A string that indicates the position at which to begin the returned list of tape pools.</p>"""
    limit: NotRequired[
        "aws_sdk_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>An optional number limit for the tape pools in the list returned by this call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTapePoolsInput) -> dict:
    out: dict = {}
    if "pool_ar_ns" in value:
        import aws_sdk_storage_gateway.types.pool_ar_ns

        out["PoolARNs"] = (
            aws_sdk_storage_gateway.types.pool_ar_ns.serialize_aws_json_1_1(
                value["pool_ar_ns"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTapePoolsInput:
    out: ListTapePoolsInput = {}  # type: ignore[typeddict-item]
    if "PoolARNs" in data:
        import aws_sdk_storage_gateway.types.pool_ar_ns

        out["pool_ar_ns"] = (
            aws_sdk_storage_gateway.types.pool_ar_ns.deserialize_aws_json_1_1(
                data["PoolARNs"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
