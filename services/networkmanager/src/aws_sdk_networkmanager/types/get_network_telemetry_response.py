"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkTelemetryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.network_telemetry_list
    import aws_sdk_networkmanager.types.next_token


class GetNetworkTelemetryResponse(TypedDict, closed=True):
    network_telemetry: NotRequired[
        "aws_sdk_networkmanager.types.network_telemetry_list.NetworkTelemetryList"
    ]
    """<p>The network telemetry.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkTelemetryResponse) -> dict:
    out: dict = {}
    if "network_telemetry" in value:
        import aws_sdk_networkmanager.types.network_telemetry_list

        out["NetworkTelemetry"] = (
            aws_sdk_networkmanager.types.network_telemetry_list.serialize_json(
                value["network_telemetry"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetNetworkTelemetryResponse:
    out: GetNetworkTelemetryResponse = {}  # type: ignore[typeddict-item]
    if "NetworkTelemetry" in data:
        import aws_sdk_networkmanager.types.network_telemetry_list

        out["network_telemetry"] = (
            aws_sdk_networkmanager.types.network_telemetry_list.deserialize_json(
                data["NetworkTelemetry"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
