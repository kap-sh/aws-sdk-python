"""Generated from Smithy shape ``com.amazonaws.guardduty#Ipv6Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

Ipv6Addresses: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: Ipv6Addresses) -> list:
    return list(value)


def deserialize_json(data: list) -> Ipv6Addresses:
    return list(data)
