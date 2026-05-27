"""Generated from Smithy shape ``com.amazonaws.ec2#ReportInstanceReasonCodes``."""

from typing import Literal, TypeAlias

ReportInstanceReasonCodes: TypeAlias = Literal[
    "instance-stuck-in-state",
    "unresponsive",
    "not-accepting-credentials",
    "password-not-available",
    "performance-network",
    "performance-instance-store",
    "performance-ebs-volume",
    "performance-other",
    "other",
]
