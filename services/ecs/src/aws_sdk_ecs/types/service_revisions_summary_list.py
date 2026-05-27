"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_revision_summary

ServiceRevisionsSummaryList: TypeAlias = list[
    "aws_sdk_ecs.types.service_revision_summary.ServiceRevisionSummary"
]
