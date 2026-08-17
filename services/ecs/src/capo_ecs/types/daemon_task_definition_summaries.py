"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_task_definition_summary

DaemonTaskDefinitionSummaries: TypeAlias = list[
    "capo_ecs.types.daemon_task_definition_summary.DaemonTaskDefinitionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonTaskDefinitionSummaries) -> list:
    import capo_ecs.types.daemon_task_definition_summary

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.daemon_task_definition_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonTaskDefinitionSummaries:
    import capo_ecs.types.daemon_task_definition_summary

    out: DaemonTaskDefinitionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.daemon_task_definition_summary.deserialize_aws_json_1_1(item)
        )
    return out
