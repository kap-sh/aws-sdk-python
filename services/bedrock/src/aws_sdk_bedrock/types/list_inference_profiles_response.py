"""Generated from Smithy shape ``com.amazonaws.bedrock#ListInferenceProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.inference_profile_summaries
    import aws_sdk_bedrock.types.pagination_token


class ListInferenceProfilesResponse(TypedDict):
    inference_profile_summaries: NotRequired[
        "aws_sdk_bedrock.types.inference_profile_summaries.InferenceProfileSummaries"
    ]
    """<p>A list of information about each inference profile that you can use.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInferenceProfilesResponse) -> dict:
    out: dict = {}
    if "inference_profile_summaries" in value:
        import aws_sdk_bedrock.types.inference_profile_summaries

        out["inferenceProfileSummaries"] = (
            aws_sdk_bedrock.types.inference_profile_summaries.serialize_json(
                value["inference_profile_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInferenceProfilesResponse:
    out: ListInferenceProfilesResponse = {}  # type: ignore[typeddict-item]
    if "inferenceProfileSummaries" in data:
        import aws_sdk_bedrock.types.inference_profile_summaries

        out["inference_profile_summaries"] = (
            aws_sdk_bedrock.types.inference_profile_summaries.deserialize_json(
                data["inferenceProfileSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
