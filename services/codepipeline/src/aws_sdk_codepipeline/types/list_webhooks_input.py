"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListWebhooksInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.max_results
    import aws_sdk_codepipeline.types.next_token


class ListWebhooksInput(TypedDict):
    next_token: NotRequired["aws_sdk_codepipeline.types.next_token.NextToken"]
    """<p>The token that was returned from the previous ListWebhooks call, which can be used to return the next set of webhooks in the list.</p>"""
    max_results: NotRequired["aws_sdk_codepipeline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWebhooksInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWebhooksInput:
    out: ListWebhooksInput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
