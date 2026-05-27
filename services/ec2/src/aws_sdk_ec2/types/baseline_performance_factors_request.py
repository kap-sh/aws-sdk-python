"""Generated from Smithy shape ``com.amazonaws.ec2#BaselinePerformanceFactorsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cpu_performance_factor_request


class BaselinePerformanceFactorsRequest(TypedDict):
    cpu: NotRequired[
        "aws_sdk_ec2.types.cpu_performance_factor_request.CpuPerformanceFactorRequest"
    ]
    """<p>The CPU performance to consider, using an instance family as the baseline reference.</p>"""
