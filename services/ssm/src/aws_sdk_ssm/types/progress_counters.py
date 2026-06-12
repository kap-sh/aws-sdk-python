"""Generated from Smithy shape ``com.amazonaws.ssm#ProgressCounters``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.integer


class ProgressCounters(TypedDict):
    total_steps: "aws_sdk_ssm.types.integer.Integer"
    """<p>The total number of steps run in all specified Amazon Web Services Regions and Amazon Web Services accounts for the current Automation execution.</p>"""
    success_steps: "aws_sdk_ssm.types.integer.Integer"
    """<p>The total number of steps that successfully completed in all specified Amazon Web Services Regions and Amazon Web Services accounts for the current Automation execution.</p>"""
    failed_steps: "aws_sdk_ssm.types.integer.Integer"
    """<p>The total number of steps that failed to run in all specified Amazon Web Services Regions and Amazon Web Services accounts for the current Automation execution.</p>"""
    cancelled_steps: "aws_sdk_ssm.types.integer.Integer"
    """<p>The total number of steps that the system cancelled in all specified Amazon Web Services Regions and Amazon Web Services accounts for the current Automation execution.</p>"""
    timed_out_steps: "aws_sdk_ssm.types.integer.Integer"
    """<p>The total number of steps that timed out in all specified Amazon Web Services Regions and Amazon Web Services accounts for the current Automation execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProgressCounters) -> dict:
    out: dict = {}
    out["TotalSteps"] = value.get("total_steps", 0)
    out["SuccessSteps"] = value.get("success_steps", 0)
    out["FailedSteps"] = value.get("failed_steps", 0)
    out["CancelledSteps"] = value.get("cancelled_steps", 0)
    out["TimedOutSteps"] = value.get("timed_out_steps", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ProgressCounters:
    out: ProgressCounters = {}  # type: ignore[typeddict-item]
    if "TotalSteps" in data:
        out["total_steps"] = data["TotalSteps"]
    else:
        out["total_steps"] = 0
    if "SuccessSteps" in data:
        out["success_steps"] = data["SuccessSteps"]
    else:
        out["success_steps"] = 0
    if "FailedSteps" in data:
        out["failed_steps"] = data["FailedSteps"]
    else:
        out["failed_steps"] = 0
    if "CancelledSteps" in data:
        out["cancelled_steps"] = data["CancelledSteps"]
    else:
        out["cancelled_steps"] = 0
    if "TimedOutSteps" in data:
        out["timed_out_steps"] = data["TimedOutSteps"]
    else:
        out["timed_out_steps"] = 0
    return out
