"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListComputeQuotasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.compute_quota_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListComputeQuotasResponse(TypedDict):
    compute_quota_summaries: NotRequired[
        "aws_sdk_sagemaker.types.compute_quota_summary_list.ComputeQuotaSummaryList"
    ]
    """<p>Summaries of the compute allocation definitions.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListComputeQuotasResponse) -> dict:
    out: dict = {}
    if "compute_quota_summaries" in value:
        import aws_sdk_sagemaker.types.compute_quota_summary_list

        out["ComputeQuotaSummaries"] = (
            aws_sdk_sagemaker.types.compute_quota_summary_list.serialize_aws_json_1_1(
                value["compute_quota_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListComputeQuotasResponse:
    out: ListComputeQuotasResponse = {}  # type: ignore[typeddict-item]
    if "ComputeQuotaSummaries" in data:
        import aws_sdk_sagemaker.types.compute_quota_summary_list

        out["compute_quota_summaries"] = (
            aws_sdk_sagemaker.types.compute_quota_summary_list.deserialize_aws_json_1_1(
                data["ComputeQuotaSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
