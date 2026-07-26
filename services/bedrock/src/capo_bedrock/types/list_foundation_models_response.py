"""Generated from Smithy shape ``com.amazonaws.bedrock#ListFoundationModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.foundation_model_summary_list


class ListFoundationModelsResponse(TypedDict, closed=True):
    model_summaries: NotRequired[
        "capo_bedrock.types.foundation_model_summary_list.FoundationModelSummaryList"
    ]
    """<p>A list of Amazon Bedrock foundation models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFoundationModelsResponse) -> dict:
    out: dict = {}
    if "model_summaries" in value:
        import capo_bedrock.types.foundation_model_summary_list

        out["modelSummaries"] = (
            capo_bedrock.types.foundation_model_summary_list.serialize_json(
                value["model_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListFoundationModelsResponse:
    out: ListFoundationModelsResponse = {}  # type: ignore[typeddict-item]
    if "modelSummaries" in data:
        import capo_bedrock.types.foundation_model_summary_list

        out["model_summaries"] = (
            capo_bedrock.types.foundation_model_summary_list.deserialize_json(
                data["modelSummaries"]
            )
        )
    return out
