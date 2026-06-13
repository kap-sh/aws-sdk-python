"""Generated from Smithy shape ``com.amazonaws.bedrock#ListFoundationModelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.foundation_model_summary_list


class ListFoundationModelsResponse(TypedDict):
    model_summaries: NotRequired[
        "aws_sdk_bedrock.types.foundation_model_summary_list.FoundationModelSummaryList"
    ]
    """<p>A list of Amazon Bedrock foundation models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFoundationModelsResponse) -> dict:
    out: dict = {}
    if "model_summaries" in value:
        import aws_sdk_bedrock.types.foundation_model_summary_list

        out["modelSummaries"] = (
            aws_sdk_bedrock.types.foundation_model_summary_list.serialize_json(
                value["model_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListFoundationModelsResponse:
    out: ListFoundationModelsResponse = {}  # type: ignore[typeddict-item]
    if "modelSummaries" in data:
        import aws_sdk_bedrock.types.foundation_model_summary_list

        out["model_summaries"] = (
            aws_sdk_bedrock.types.foundation_model_summary_list.deserialize_json(
                data["modelSummaries"]
            )
        )
    return out
