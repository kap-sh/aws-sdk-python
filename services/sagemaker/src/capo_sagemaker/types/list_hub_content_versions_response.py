"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListHubContentVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_content_info_list
    import capo_sagemaker.types.next_token


class ListHubContentVersionsResponse(TypedDict, closed=True):
    hub_content_summaries: NotRequired[
        "capo_sagemaker.types.hub_content_info_list.HubContentInfoList"
    ]
    """<p>The summaries of the listed hub content versions.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of hub content versions, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHubContentVersionsResponse) -> dict:
    out: dict = {}
    if "hub_content_summaries" in value:
        import capo_sagemaker.types.hub_content_info_list

        out["HubContentSummaries"] = (
            capo_sagemaker.types.hub_content_info_list.serialize_aws_json_1_1(
                value["hub_content_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHubContentVersionsResponse:
    out: ListHubContentVersionsResponse = {}  # type: ignore[typeddict-item]
    if "HubContentSummaries" in data:
        import capo_sagemaker.types.hub_content_info_list

        out["hub_content_summaries"] = (
            capo_sagemaker.types.hub_content_info_list.deserialize_aws_json_1_1(
                data["HubContentSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
