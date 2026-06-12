"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryTriggersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_trigger

RepositoryTriggersList: TypeAlias = list[
    "aws_sdk_codecommit.types.repository_trigger.RepositoryTrigger"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryTriggersList) -> list:
    import aws_sdk_codecommit.types.repository_trigger

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.repository_trigger.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryTriggersList:
    import aws_sdk_codecommit.types.repository_trigger

    out: RepositoryTriggersList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.repository_trigger.deserialize_aws_json_1_1(item)
        )
    return out
