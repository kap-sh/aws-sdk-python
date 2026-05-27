"""Generated from Smithy shape ``com.amazonaws.ecs#SecretList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.secret

SecretList: TypeAlias = list["aws_sdk_ecs.types.secret.Secret"]
