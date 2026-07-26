"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryTriggerExecutionFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.repository_trigger_execution_failure

RepositoryTriggerExecutionFailureList: TypeAlias = list[
    "capo_codecommit.types.repository_trigger_execution_failure.RepositoryTriggerExecutionFailure"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryTriggerExecutionFailureList) -> list:
    import capo_codecommit.types.repository_trigger_execution_failure

    out: list = []
    for item in value:
        out.append(
            capo_codecommit.types.repository_trigger_execution_failure.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryTriggerExecutionFailureList:
    import capo_codecommit.types.repository_trigger_execution_failure

    out: RepositoryTriggerExecutionFailureList = []
    for item in data:
        out.append(
            capo_codecommit.types.repository_trigger_execution_failure.deserialize_aws_json_1_1(
                item
            )
        )
    return out
