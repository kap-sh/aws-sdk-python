"""Generated from Smithy shape ``com.amazonaws.panorama#NtpServerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.ip_address_or_server_name

NtpServerList: TypeAlias = list[
    "aws_sdk_panorama.types.ip_address_or_server_name.IpAddressOrServerName"
]


# --- restJson1 ser/de ---
def serialize_json(value: NtpServerList) -> list:
    return list(value)


def deserialize_json(data: list) -> NtpServerList:
    return list(data)
