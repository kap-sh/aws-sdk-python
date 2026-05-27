"""Generated from Smithy shape ``com.amazonaws.ecs#Statistics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.key_value_pair

Statistics: TypeAlias = list["aws_sdk_ecs.types.key_value_pair.KeyValuePair"]
