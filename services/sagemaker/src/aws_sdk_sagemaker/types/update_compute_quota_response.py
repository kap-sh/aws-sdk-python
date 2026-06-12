"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateComputeQuotaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.compute_quota_arn
    import aws_sdk_sagemaker.types.integer


class UpdateComputeQuotaResponse(TypedDict):
    compute_quota_arn: NotRequired[
        "aws_sdk_sagemaker.types.compute_quota_arn.ComputeQuotaArn"
    ]
    """<p>ARN of the compute allocation definition.</p>"""
    compute_quota_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>Version of the compute allocation definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateComputeQuotaResponse) -> dict:
    out: dict = {}
    if "compute_quota_arn" in value:
        out["ComputeQuotaArn"] = value["compute_quota_arn"]
    if "compute_quota_version" in value:
        out["ComputeQuotaVersion"] = value["compute_quota_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateComputeQuotaResponse:
    out: UpdateComputeQuotaResponse = {}  # type: ignore[typeddict-item]
    if "ComputeQuotaArn" in data:
        out["compute_quota_arn"] = data["ComputeQuotaArn"]
    if "ComputeQuotaVersion" in data:
        out["compute_quota_version"] = data["ComputeQuotaVersion"]
    return out
