"""Generated from Smithy shape ``com.amazonaws.groundstation#RangedSocketAddress``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.integer_range
    import aws_sdk_groundstation.types.ip_v4_address


class RangedSocketAddress(TypedDict):
    name: "aws_sdk_groundstation.types.ip_v4_address.IpV4Address"
    """<p>IPv4 socket address.</p>"""
    port_range: "aws_sdk_groundstation.types.integer_range.IntegerRange"
    """<p>Port range of a socket address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RangedSocketAddress) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_groundstation.types.integer_range

    out["portRange"] = aws_sdk_groundstation.types.integer_range.serialize_json(
        value["port_range"]
    )
    return out


def deserialize_json(data: dict) -> RangedSocketAddress:
    out: RangedSocketAddress = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RangedSocketAddress.name required")
    if "portRange" in data:
        import aws_sdk_groundstation.types.integer_range

        out["port_range"] = aws_sdk_groundstation.types.integer_range.deserialize_json(
            data["portRange"]
        )
    else:
        raise DeserializationError("RangedSocketAddress.port_range required")
    return out
