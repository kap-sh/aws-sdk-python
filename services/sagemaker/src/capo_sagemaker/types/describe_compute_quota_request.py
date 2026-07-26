"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeComputeQuotaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.compute_quota_id
    import capo_sagemaker.types.integer


class DescribeComputeQuotaRequest(TypedDict, closed=True):
    compute_quota_id: NotRequired[
        "capo_sagemaker.types.compute_quota_id.ComputeQuotaId"
    ]
    """<p>ID of the compute allocation definition.</p>"""
    compute_quota_version: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>Version of the compute allocation definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComputeQuotaRequest) -> dict:
    out: dict = {}
    if "compute_quota_id" in value:
        out["ComputeQuotaId"] = value["compute_quota_id"]
    if "compute_quota_version" in value:
        out["ComputeQuotaVersion"] = value["compute_quota_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComputeQuotaRequest:
    out: DescribeComputeQuotaRequest = {}  # type: ignore[typeddict-item]
    if "ComputeQuotaId" in data:
        out["compute_quota_id"] = data["ComputeQuotaId"]
    if "ComputeQuotaVersion" in data:
        out["compute_quota_version"] = data["ComputeQuotaVersion"]
    return out
