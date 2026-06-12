"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkConnection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.network_direction


class NetworkConnection(TypedDict):
    direction: NotRequired["aws_sdk_guardduty.types.network_direction.NetworkDirection"]
    """<p>The direction in which the network traffic is flowing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnection) -> dict:
    out: dict = {}
    if "direction" in value:
        import aws_sdk_guardduty.types.network_direction

        out["direction"] = aws_sdk_guardduty.types.network_direction.serialize_json(
            value["direction"]
        )
    return out


def deserialize_json(data: dict) -> NetworkConnection:
    out: NetworkConnection = {}  # type: ignore[typeddict-item]
    if "direction" in data:
        import aws_sdk_guardduty.types.network_direction

        out["direction"] = aws_sdk_guardduty.types.network_direction.deserialize_json(
            data["direction"]
        )
    return out
