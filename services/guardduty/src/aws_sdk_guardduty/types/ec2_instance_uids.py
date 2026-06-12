"""Generated from Smithy shape ``com.amazonaws.guardduty#Ec2InstanceUids``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.ec2_instance_uid

Ec2InstanceUids: TypeAlias = list[
    "aws_sdk_guardduty.types.ec2_instance_uid.Ec2InstanceUid"
]


# --- restJson1 ser/de ---
def serialize_json(value: Ec2InstanceUids) -> list:
    return list(value)


def deserialize_json(data: list) -> Ec2InstanceUids:
    return list(data)
