"""Generated from Smithy shape ``com.amazonaws.groundstation#RangedConnectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ranged_socket_address


class RangedConnectionDetails(TypedDict, closed=True):
    socket_address: (
        "aws_sdk_groundstation.types.ranged_socket_address.RangedSocketAddress"
    )
    """<p>A ranged socket address.</p>"""
    mtu: NotRequired["int"]
    """<p>Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RangedConnectionDetails) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.ranged_socket_address

    out["socketAddress"] = (
        aws_sdk_groundstation.types.ranged_socket_address.serialize_json(
            value["socket_address"]
        )
    )
    if "mtu" in value:
        out["mtu"] = value["mtu"]
    return out


def deserialize_json(data: dict) -> RangedConnectionDetails:
    out: RangedConnectionDetails = {}  # type: ignore[typeddict-item]
    if "socketAddress" in data:
        import aws_sdk_groundstation.types.ranged_socket_address

        out["socket_address"] = (
            aws_sdk_groundstation.types.ranged_socket_address.deserialize_json(
                data["socketAddress"]
            )
        )
    else:
        raise DeserializationError("RangedConnectionDetails.socket_address required")
    if "mtu" in data:
        out["mtu"] = data["mtu"]
    return out
