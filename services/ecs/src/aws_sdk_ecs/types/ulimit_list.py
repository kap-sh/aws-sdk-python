"""Generated from Smithy shape ``com.amazonaws.ecs#UlimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ulimit

UlimitList: TypeAlias = list["aws_sdk_ecs.types.ulimit.Ulimit"]
