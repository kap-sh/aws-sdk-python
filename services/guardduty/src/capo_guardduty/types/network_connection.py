"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.network_direction


class NetworkConnection(TypedDict, closed=True):
    direction: NotRequired["capo_guardduty.types.network_direction.NetworkDirection"]
    """<p>The direction in which the network traffic is flowing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnection) -> dict:
    out: dict = {}
    if "direction" in value:
        import capo_guardduty.types.network_direction

        out["direction"] = capo_guardduty.types.network_direction.serialize_json(
            value["direction"]
        )
    return out


def deserialize_json(data: dict) -> NetworkConnection:
    out: NetworkConnection = {}  # type: ignore[typeddict-item]
    if "direction" in data:
        import capo_guardduty.types.network_direction

        out["direction"] = capo_guardduty.types.network_direction.deserialize_json(
            data["direction"]
        )
    return out
