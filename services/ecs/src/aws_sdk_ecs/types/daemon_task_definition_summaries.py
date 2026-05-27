"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_task_definition_summary

DaemonTaskDefinitionSummaries: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_task_definition_summary.DaemonTaskDefinitionSummary"
]
