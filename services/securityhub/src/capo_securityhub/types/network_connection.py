"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.connection_direction


class NetworkConnection(TypedDict, closed=True):
    direction: NotRequired[
        "capo_securityhub.types.connection_direction.ConnectionDirection"
    ]
    """<p> The direction in which the network traffic is flowing. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnection) -> dict:
    out: dict = {}
    if "direction" in value:
        import capo_securityhub.types.connection_direction

        out["Direction"] = capo_securityhub.types.connection_direction.serialize_json(
            value["direction"]
        )
    return out


def deserialize_json(data: dict) -> NetworkConnection:
    out: NetworkConnection = {}  # type: ignore[typeddict-item]
    if "Direction" in data:
        import capo_securityhub.types.connection_direction

        out["direction"] = capo_securityhub.types.connection_direction.deserialize_json(
            data["Direction"]
        )
    return out
