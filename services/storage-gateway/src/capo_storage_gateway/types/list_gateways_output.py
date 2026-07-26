"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListGatewaysOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateways
    import capo_storage_gateway.types.marker


class ListGatewaysOutput(TypedDict, closed=True):
    gateways: NotRequired["capo_storage_gateway.types.gateways.Gateways"]
    """<p>An array of <a>GatewayInfo</a> objects.</p>"""
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>Use the marker in your next request to fetch the next set of gateways in the list. If there are no more gateways to list, this field does not appear in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGatewaysOutput) -> dict:
    out: dict = {}
    if "gateways" in value:
        import capo_storage_gateway.types.gateways

        out["Gateways"] = capo_storage_gateway.types.gateways.serialize_aws_json_1_1(
            value["gateways"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGatewaysOutput:
    out: ListGatewaysOutput = {}  # type: ignore[typeddict-item]
    if "Gateways" in data:
        import capo_storage_gateway.types.gateways

        out["gateways"] = capo_storage_gateway.types.gateways.deserialize_aws_json_1_1(
            data["Gateways"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
