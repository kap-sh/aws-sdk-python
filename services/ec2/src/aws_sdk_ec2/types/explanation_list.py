"""Generated from Smithy shape ``com.amazonaws.ec2#ExplanationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.explanation

ExplanationList: TypeAlias = list["aws_sdk_ec2.types.explanation.Explanation"]
