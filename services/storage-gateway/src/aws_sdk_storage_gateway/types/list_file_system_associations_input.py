"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListFileSystemAssociationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.positive_int_object


class ListFileSystemAssociationsInput(TypedDict, closed=True):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    limit: NotRequired[
        "aws_sdk_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>The maximum number of file system associations to return in the response. If present, <code>Limit</code> must be an integer with a value greater than zero. Optional.</p>"""
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>Opaque pagination token returned from a previous <code>ListFileSystemAssociations</code> operation. If present, <code>Marker</code> specifies where to continue the list from after a previous call to <code>ListFileSystemAssociations</code>. Optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFileSystemAssociationsInput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFileSystemAssociationsInput:
    out: ListFileSystemAssociationsInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
