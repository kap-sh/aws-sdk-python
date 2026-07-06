"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListContextsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.context_summaries
    import aws_sdk_sagemaker.types.next_token


class ListContextsResponse(TypedDict, closed=True):
    context_summaries: NotRequired[
        "aws_sdk_sagemaker.types.context_summaries.ContextSummaries"
    ]
    """<p>A list of contexts and their properties.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of contexts, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContextsResponse) -> dict:
    out: dict = {}
    if "context_summaries" in value:
        import aws_sdk_sagemaker.types.context_summaries

        out["ContextSummaries"] = (
            aws_sdk_sagemaker.types.context_summaries.serialize_aws_json_1_1(
                value["context_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContextsResponse:
    out: ListContextsResponse = {}  # type: ignore[typeddict-item]
    if "ContextSummaries" in data:
        import aws_sdk_sagemaker.types.context_summaries

        out["context_summaries"] = (
            aws_sdk_sagemaker.types.context_summaries.deserialize_aws_json_1_1(
                data["ContextSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
