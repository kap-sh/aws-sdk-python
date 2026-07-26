"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryTriggerEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.repository_trigger_event_enum

RepositoryTriggerEventList: TypeAlias = list[
    "capo_codecommit.types.repository_trigger_event_enum.RepositoryTriggerEventEnum"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryTriggerEventList) -> list:
    import capo_codecommit.types.repository_trigger_event_enum

    out: list = []
    for item in value:
        out.append(
            capo_codecommit.types.repository_trigger_event_enum.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryTriggerEventList:
    import capo_codecommit.types.repository_trigger_event_enum

    out: RepositoryTriggerEventList = []
    for item in data:
        out.append(
            capo_codecommit.types.repository_trigger_event_enum.deserialize_aws_json_1_1(
                item
            )
        )
    return out
