"""Generated from Smithy shape ``com.amazonaws.ec2#ErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.validation_error

ErrorSet: TypeAlias = list["aws_sdk_ec2.types.validation_error.ValidationError"]
