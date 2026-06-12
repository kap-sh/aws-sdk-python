"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryTriggerNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_trigger_name

RepositoryTriggerNameList: TypeAlias = list[
    "aws_sdk_codecommit.types.repository_trigger_name.RepositoryTriggerName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryTriggerNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RepositoryTriggerNameList:
    return list(data)
