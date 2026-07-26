"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListVolumesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.marker
    import capo_storage_gateway.types.positive_int_object


class ListVolumesInput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>A string that indicates the position at which to begin the returned list of volumes. Obtain the marker from the response of a previous List iSCSI Volumes request.</p>"""
    limit: NotRequired[
        "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>Specifies that the list of volumes returned be limited to the specified number of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVolumesInput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVolumesInput:
    out: ListVolumesInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
