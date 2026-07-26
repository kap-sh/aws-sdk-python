"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateComputeQuotaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.compute_quota_arn
    import capo_sagemaker.types.compute_quota_id


class CreateComputeQuotaResponse(TypedDict, closed=True):
    compute_quota_arn: NotRequired[
        "capo_sagemaker.types.compute_quota_arn.ComputeQuotaArn"
    ]
    """<p>ARN of the compute allocation definition.</p>"""
    compute_quota_id: NotRequired[
        "capo_sagemaker.types.compute_quota_id.ComputeQuotaId"
    ]
    """<p>ID of the compute allocation definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateComputeQuotaResponse) -> dict:
    out: dict = {}
    if "compute_quota_arn" in value:
        out["ComputeQuotaArn"] = value["compute_quota_arn"]
    if "compute_quota_id" in value:
        out["ComputeQuotaId"] = value["compute_quota_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateComputeQuotaResponse:
    out: CreateComputeQuotaResponse = {}  # type: ignore[typeddict-item]
    if "ComputeQuotaArn" in data:
        out["compute_quota_arn"] = data["ComputeQuotaArn"]
    if "ComputeQuotaId" in data:
        out["compute_quota_id"] = data["ComputeQuotaId"]
    return out
