"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EC2InstanceError``."""

from typing_extensions import NotRequired, TypedDict


class EC2InstanceError(TypedDict, closed=True):
    ec2_error_code: NotRequired["str"]
    """<p>Unique error code identifying the specific EC2 instance error.</p>"""
    ec2_exception_type: NotRequired["str"]
    """<p>Type of exception encountered during EC2 instance operation.</p>"""
    ec2_error_message: NotRequired["str"]
    """<p>Detailed description of the EC2 instance error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EC2InstanceError) -> dict:
    out: dict = {}
    if "ec2_error_code" in value:
        out["EC2ErrorCode"] = value["ec2_error_code"]
    if "ec2_exception_type" in value:
        out["EC2ExceptionType"] = value["ec2_exception_type"]
    if "ec2_error_message" in value:
        out["EC2ErrorMessage"] = value["ec2_error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EC2InstanceError:
    out: EC2InstanceError = {}  # type: ignore[typeddict-item]
    if "EC2ErrorCode" in data:
        out["ec2_error_code"] = data["EC2ErrorCode"]
    if "EC2ExceptionType" in data:
        out["ec2_exception_type"] = data["EC2ExceptionType"]
    if "EC2ErrorMessage" in data:
        out["ec2_error_message"] = data["EC2ErrorMessage"]
    return out
