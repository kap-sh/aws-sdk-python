"""Generated from Smithy shape ``com.amazonaws.ec2#DeclarativePoliciesReportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.declarative_policies_report

DeclarativePoliciesReportList: TypeAlias = list[
    "aws_sdk_ec2.types.declarative_policies_report.DeclarativePoliciesReport"
]
