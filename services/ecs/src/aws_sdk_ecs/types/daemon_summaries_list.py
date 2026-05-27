"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_summary

DaemonSummariesList: TypeAlias = list["aws_sdk_ecs.types.daemon_summary.DaemonSummary"]
