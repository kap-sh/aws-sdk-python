"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.protection_group

ProtectionGroups: TypeAlias = list[
    "aws_sdk_shield.types.protection_group.ProtectionGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroups) -> list:
    import aws_sdk_shield.types.protection_group

    out: list = []
    for item in value:
        out.append(aws_sdk_shield.types.protection_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectionGroups:
    import aws_sdk_shield.types.protection_group

    out: ProtectionGroups = []
    for item in data:
        out.append(aws_sdk_shield.types.protection_group.deserialize_aws_json_1_1(item))
    return out
