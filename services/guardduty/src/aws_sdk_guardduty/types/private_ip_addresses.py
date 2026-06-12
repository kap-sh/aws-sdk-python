"""Generated from Smithy shape ``com.amazonaws.guardduty#PrivateIpAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.private_ip_address_details

PrivateIpAddresses: TypeAlias = list[
    "aws_sdk_guardduty.types.private_ip_address_details.PrivateIpAddressDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateIpAddresses) -> list:
    import aws_sdk_guardduty.types.private_ip_address_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.private_ip_address_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PrivateIpAddresses:
    import aws_sdk_guardduty.types.private_ip_address_details

    out: PrivateIpAddresses = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.private_ip_address_details.deserialize_json(item)
        )
    return out
