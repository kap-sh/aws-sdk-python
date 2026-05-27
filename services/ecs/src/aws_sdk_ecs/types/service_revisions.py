"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_revision

ServiceRevisions: TypeAlias = list["aws_sdk_ecs.types.service_revision.ServiceRevision"]
