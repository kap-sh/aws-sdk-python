"""Generated from Smithy shape ``com.amazonaws.ecs#AttachmentDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.key_value_pair

AttachmentDetails: TypeAlias = list["aws_sdk_ecs.types.key_value_pair.KeyValuePair"]
