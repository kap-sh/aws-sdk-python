"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListGatewaysInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.marker
    import capo_storage_gateway.types.positive_int_object


class ListGatewaysInput(TypedDict, closed=True):
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which to begin the returned list of gateways.</p>"""
    limit: NotRequired[
        "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>Specifies that the list of gateways returned be limited to the specified number of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGatewaysInput) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGatewaysInput:
    out: ListGatewaysInput = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
