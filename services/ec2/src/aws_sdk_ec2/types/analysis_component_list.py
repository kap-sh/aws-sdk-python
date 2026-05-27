"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.analysis_component

AnalysisComponentList: TypeAlias = list[
    "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
]
