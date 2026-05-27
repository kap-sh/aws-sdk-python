"""Generated from Smithy shape ``com.amazonaws.ecs#EnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.key_value_pair

EnvironmentVariables: TypeAlias = list["aws_sdk_ecs.types.key_value_pair.KeyValuePair"]
