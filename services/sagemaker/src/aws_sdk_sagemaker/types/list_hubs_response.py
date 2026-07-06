"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListHubsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_info_list
    import aws_sdk_sagemaker.types.next_token


class ListHubsResponse(TypedDict, closed=True):
    hub_summaries: NotRequired["aws_sdk_sagemaker.types.hub_info_list.HubInfoList"]
    """<p>The summaries of the listed hubs.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of hubs, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHubsResponse) -> dict:
    out: dict = {}
    if "hub_summaries" in value:
        import aws_sdk_sagemaker.types.hub_info_list

        out["HubSummaries"] = (
            aws_sdk_sagemaker.types.hub_info_list.serialize_aws_json_1_1(
                value["hub_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHubsResponse:
    out: ListHubsResponse = {}  # type: ignore[typeddict-item]
    if "HubSummaries" in data:
        import aws_sdk_sagemaker.types.hub_info_list

        out["hub_summaries"] = (
            aws_sdk_sagemaker.types.hub_info_list.deserialize_aws_json_1_1(
                data["HubSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
