"""Generated from Smithy shape ``com.amazonaws.panorama#StaticIpConnectionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.default_gateway
    import aws_sdk_panorama.types.dns_list
    import aws_sdk_panorama.types.ip_address
    import aws_sdk_panorama.types.mask


class StaticIpConnectionInfo(TypedDict, closed=True):
    ip_address: "aws_sdk_panorama.types.ip_address.IpAddress"
    """<p>The connection's IP address.</p>"""
    mask: "aws_sdk_panorama.types.mask.Mask"
    """<p>The connection's DNS mask.</p>"""
    dns: "aws_sdk_panorama.types.dns_list.DnsList"
    """<p>The connection's DNS address.</p>"""
    default_gateway: "aws_sdk_panorama.types.default_gateway.DefaultGateway"
    """<p>The connection's default gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticIpConnectionInfo) -> dict:
    out: dict = {}
    out["IpAddress"] = value["ip_address"]
    out["Mask"] = value["mask"]
    import aws_sdk_panorama.types.dns_list

    out["Dns"] = aws_sdk_panorama.types.dns_list.serialize_json(value["dns"])
    out["DefaultGateway"] = value["default_gateway"]
    return out


def deserialize_json(data: dict) -> StaticIpConnectionInfo:
    out: StaticIpConnectionInfo = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    else:
        raise DeserializationError("StaticIpConnectionInfo.ip_address required")
    if "Mask" in data:
        out["mask"] = data["Mask"]
    else:
        raise DeserializationError("StaticIpConnectionInfo.mask required")
    if "Dns" in data:
        import aws_sdk_panorama.types.dns_list

        out["dns"] = aws_sdk_panorama.types.dns_list.deserialize_json(data["Dns"])
    else:
        raise DeserializationError("StaticIpConnectionInfo.dns required")
    if "DefaultGateway" in data:
        out["default_gateway"] = data["DefaultGateway"]
    else:
        raise DeserializationError("StaticIpConnectionInfo.default_gateway required")
    return out
