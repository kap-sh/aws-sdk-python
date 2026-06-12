"""Generated from Smithy shape ``com.amazonaws.guardduty#Ec2NetworkInterfaceUids``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

Ec2NetworkInterfaceUids: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: Ec2NetworkInterfaceUids) -> list:
    return list(value)


def deserialize_json(data: list) -> Ec2NetworkInterfaceUids:
    return list(data)
