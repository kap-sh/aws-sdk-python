"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDescribeModelPackageError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string


class BatchDescribeModelPackageError(TypedDict, closed=True):
    error_code: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p/>"""
    error_response: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p/>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDescribeModelPackageError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_response" in value:
        out["ErrorResponse"] = value["error_response"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeModelPackageError:
    out: BatchDescribeModelPackageError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorResponse" in data:
        out["error_response"] = data["ErrorResponse"]
    return out
