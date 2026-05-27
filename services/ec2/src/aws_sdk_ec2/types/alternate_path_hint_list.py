"""Generated from Smithy shape ``com.amazonaws.ec2#AlternatePathHintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.alternate_path_hint

AlternatePathHintList: TypeAlias = list[
    "aws_sdk_ec2.types.alternate_path_hint.AlternatePathHint"
]
