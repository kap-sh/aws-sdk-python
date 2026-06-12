"""Generated from Smithy shape ``com.amazonaws.deadline#IpAddresses``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.ip_v4_addresses
    import aws_sdk_deadline.types.ip_v6_addresses


class IpAddresses(TypedDict):
    ip_v4_addresses: NotRequired["aws_sdk_deadline.types.ip_v4_addresses.IpV4Addresses"]
    """<p>The IpV4 address of the network.</p>"""
    ip_v6_addresses: NotRequired["aws_sdk_deadline.types.ip_v6_addresses.IpV6Addresses"]
    """<p>The IpV6 address for the network and node component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpAddresses) -> dict:
    out: dict = {}
    if "ip_v4_addresses" in value:
        import aws_sdk_deadline.types.ip_v4_addresses

        out["ipV4Addresses"] = aws_sdk_deadline.types.ip_v4_addresses.serialize_json(
            value["ip_v4_addresses"]
        )
    if "ip_v6_addresses" in value:
        import aws_sdk_deadline.types.ip_v6_addresses

        out["ipV6Addresses"] = aws_sdk_deadline.types.ip_v6_addresses.serialize_json(
            value["ip_v6_addresses"]
        )
    return out


def deserialize_json(data: dict) -> IpAddresses:
    out: IpAddresses = {}  # type: ignore[typeddict-item]
    if "ipV4Addresses" in data:
        import aws_sdk_deadline.types.ip_v4_addresses

        out["ip_v4_addresses"] = (
            aws_sdk_deadline.types.ip_v4_addresses.deserialize_json(
                data["ipV4Addresses"]
            )
        )
    if "ipV6Addresses" in data:
        import aws_sdk_deadline.types.ip_v6_addresses

        out["ip_v6_addresses"] = (
            aws_sdk_deadline.types.ip_v6_addresses.deserialize_json(
                data["ipV6Addresses"]
            )
        )
    return out
