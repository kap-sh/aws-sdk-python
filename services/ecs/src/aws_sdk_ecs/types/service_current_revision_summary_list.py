"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceCurrentRevisionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_current_revision_summary

ServiceCurrentRevisionSummaryList: TypeAlias = list[
    "aws_sdk_ecs.types.service_current_revision_summary.ServiceCurrentRevisionSummary"
]
