"""Generated from Smithy shape ``com.amazonaws.workmail#TargetUsers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.entity_identifier

TargetUsers: TypeAlias = list[
    "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetUsers) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetUsers:
    return list(data)
