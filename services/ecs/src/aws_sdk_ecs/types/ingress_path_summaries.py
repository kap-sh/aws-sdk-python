"""Generated from Smithy shape ``com.amazonaws.ecs#IngressPathSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ingress_path_summary

IngressPathSummaries: TypeAlias = list[
    "aws_sdk_ecs.types.ingress_path_summary.IngressPathSummary"
]
