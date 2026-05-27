"""Generated from Smithy shape ``com.amazonaws.ec2#BaselinePerformanceFactors``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cpu_performance_factor


class BaselinePerformanceFactors(TypedDict):
    cpu: NotRequired["aws_sdk_ec2.types.cpu_performance_factor.CpuPerformanceFactor"]
    """<p>The CPU performance to consider, using an instance family as the baseline reference.</p>"""
