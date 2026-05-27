"""Generated from Smithy shape ``com.amazonaws.ec2#CpuPerformanceFactor``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.performance_factor_reference_set


class CpuPerformanceFactor(TypedDict):
    references: NotRequired[
        "aws_sdk_ec2.types.performance_factor_reference_set.PerformanceFactorReferenceSet"
    ]
    """<p>Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.</p> <note> <p>Currently, only one instance family can be specified in the list.</p> </note>"""
