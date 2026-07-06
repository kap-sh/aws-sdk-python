"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceNetworkSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.input_device_ip_scheme


class InputDeviceNetworkSettings(TypedDict, closed=True):
    dns_addresses: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """The DNS addresses of the input device."""
    gateway: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The network gateway IP address."""
    ip_address: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The IP address of the input device."""
    ip_scheme: NotRequired[
        "aws_sdk_medialive.types.input_device_ip_scheme.InputDeviceIpScheme"
    ]
    """Specifies whether the input device has been configured (outside of MediaLive) to use a dynamic IP address assignment (DHCP) or a static IP address."""
    subnet_mask: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The subnet mask of the input device."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceNetworkSettings) -> dict:
    out: dict = {}
    if "dns_addresses" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["dnsAddresses"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["dns_addresses"]
        )
    if "gateway" in value:
        out["gateway"] = value["gateway"]
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "ip_scheme" in value:
        import aws_sdk_medialive.types.input_device_ip_scheme

        out["ipScheme"] = aws_sdk_medialive.types.input_device_ip_scheme.serialize_json(
            value["ip_scheme"]
        )
    if "subnet_mask" in value:
        out["subnetMask"] = value["subnet_mask"]
    return out


def deserialize_json(data: dict) -> InputDeviceNetworkSettings:
    out: InputDeviceNetworkSettings = {}  # type: ignore[typeddict-item]
    if "dnsAddresses" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["dns_addresses"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["dnsAddresses"]
            )
        )
    if "gateway" in data:
        out["gateway"] = data["gateway"]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "ipScheme" in data:
        import aws_sdk_medialive.types.input_device_ip_scheme

        out["ip_scheme"] = (
            aws_sdk_medialive.types.input_device_ip_scheme.deserialize_json(
                data["ipScheme"]
            )
        )
    if "subnetMask" in data:
        out["subnet_mask"] = data["subnetMask"]
    return out
