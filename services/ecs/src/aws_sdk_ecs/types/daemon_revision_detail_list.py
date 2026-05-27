"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRevisionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_revision_detail

DaemonRevisionDetailList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_revision_detail.DaemonRevisionDetail"
]
