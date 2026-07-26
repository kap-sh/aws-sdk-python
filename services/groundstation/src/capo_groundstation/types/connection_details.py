"""Generated from Smithy shape ``com.amazonaws.groundstation#ConnectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.socket_address


class ConnectionDetails(TypedDict, closed=True):
    socket_address: "capo_groundstation.types.socket_address.SocketAddress"
    """<p>A socket address.</p>"""
    mtu: NotRequired["int"]
    """<p>Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionDetails) -> dict:
    out: dict = {}
    import capo_groundstation.types.socket_address

    out["socketAddress"] = capo_groundstation.types.socket_address.serialize_json(
        value["socket_address"]
    )
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    return out


def deserialize_json(data: dict) -> ConnectionDetails:
    out: ConnectionDetails = {}  # type: ignore[typeddict-item]
    if "socketAddress" in data:
        import capo_groundstation.types.socket_address

        out["socket_address"] = (
            capo_groundstation.types.socket_address.deserialize_json(
                data["socketAddress"]
            )
        )
    else:
        raise DeserializationError("ConnectionDetails.socket_address required")
    if "mtu" in data:
        out["mtu"] = data["mtu"]
    return out
