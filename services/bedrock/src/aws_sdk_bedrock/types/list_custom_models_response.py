"""Generated from Smithy shape ``com.amazonaws.bedrock#ListCustomModelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_summary_list
    import aws_sdk_bedrock.types.pagination_token


class ListCustomModelsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""
    model_summaries: NotRequired[
        "aws_sdk_bedrock.types.custom_model_summary_list.CustomModelSummaryList"
    ]
    """<p>Model summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "model_summaries" in value:
        import aws_sdk_bedrock.types.custom_model_summary_list

        out["modelSummaries"] = (
            aws_sdk_bedrock.types.custom_model_summary_list.serialize_json(
                value["model_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCustomModelsResponse:
    out: ListCustomModelsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "modelSummaries" in data:
        import aws_sdk_bedrock.types.custom_model_summary_list

        out["model_summaries"] = (
            aws_sdk_bedrock.types.custom_model_summary_list.deserialize_json(
                data["modelSummaries"]
            )
        )
    return out
