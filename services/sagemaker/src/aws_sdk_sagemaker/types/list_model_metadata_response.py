"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_metadata_summaries
    import aws_sdk_sagemaker.types.next_token


class ListModelMetadataResponse(TypedDict):
    model_metadata_summaries: NotRequired[
        "aws_sdk_sagemaker.types.model_metadata_summaries.ModelMetadataSummaries"
    ]
    """<p>A structure that holds model metadata.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of recommendations, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelMetadataResponse) -> dict:
    out: dict = {}
    if "model_metadata_summaries" in value:
        import aws_sdk_sagemaker.types.model_metadata_summaries

        out["ModelMetadataSummaries"] = (
            aws_sdk_sagemaker.types.model_metadata_summaries.serialize_aws_json_1_1(
                value["model_metadata_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelMetadataResponse:
    out: ListModelMetadataResponse = {}  # type: ignore[typeddict-item]
    if "ModelMetadataSummaries" in data:
        import aws_sdk_sagemaker.types.model_metadata_summaries

        out["model_metadata_summaries"] = (
            aws_sdk_sagemaker.types.model_metadata_summaries.deserialize_aws_json_1_1(
                data["ModelMetadataSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
