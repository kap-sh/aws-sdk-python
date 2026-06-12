"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupIdFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.protection_group_id

ProtectionGroupIdFilters: TypeAlias = list[
    "aws_sdk_shield.types.protection_group_id.ProtectionGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupIdFilters) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProtectionGroupIdFilters:
    return list(data)
