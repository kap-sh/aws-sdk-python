"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryTriggerEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_trigger_event_enum

RepositoryTriggerEventList: TypeAlias = list[
    "aws_sdk_codecommit.types.repository_trigger_event_enum.RepositoryTriggerEventEnum"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryTriggerEventList) -> list:
    import aws_sdk_codecommit.types.repository_trigger_event_enum

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.repository_trigger_event_enum.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryTriggerEventList:
    import aws_sdk_codecommit.types.repository_trigger_event_enum

    out: RepositoryTriggerEventList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.repository_trigger_event_enum.deserialize_aws_json_1_1(
                item
            )
        )
    return out
