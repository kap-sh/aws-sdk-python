"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_metadata_summaries
    import capo_sagemaker.types.next_token


class ListModelMetadataResponse(TypedDict, closed=True):
    model_metadata_summaries: NotRequired[
        "capo_sagemaker.types.model_metadata_summaries.ModelMetadataSummaries"
    ]
    """<p>A structure that holds model metadata.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of recommendations, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelMetadataResponse) -> dict:
    out: dict = {}
    if "model_metadata_summaries" in value:
        import capo_sagemaker.types.model_metadata_summaries

        out["ModelMetadataSummaries"] = (
            capo_sagemaker.types.model_metadata_summaries.serialize_aws_json_1_1(
                value["model_metadata_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelMetadataResponse:
    out: ListModelMetadataResponse = {}  # type: ignore[typeddict-item]
    if "ModelMetadataSummaries" in data:
        import capo_sagemaker.types.model_metadata_summaries

        out["model_metadata_summaries"] = (
            capo_sagemaker.types.model_metadata_summaries.deserialize_aws_json_1_1(
                data["ModelMetadataSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
