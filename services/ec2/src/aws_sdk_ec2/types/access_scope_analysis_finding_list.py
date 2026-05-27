"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopeAnalysisFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.access_scope_analysis_finding

AccessScopeAnalysisFindingList: TypeAlias = list[
    "aws_sdk_ec2.types.access_scope_analysis_finding.AccessScopeAnalysisFinding"
]
