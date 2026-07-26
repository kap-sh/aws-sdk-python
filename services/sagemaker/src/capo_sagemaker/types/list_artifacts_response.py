"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListArtifactsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.artifact_summaries
    import capo_sagemaker.types.next_token


class ListArtifactsResponse(TypedDict, closed=True):
    artifact_summaries: NotRequired[
        "capo_sagemaker.types.artifact_summaries.ArtifactSummaries"
    ]
    """<p>A list of artifacts and their properties.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of artifacts, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListArtifactsResponse) -> dict:
    out: dict = {}
    if "artifact_summaries" in value:
        import capo_sagemaker.types.artifact_summaries

        out["ArtifactSummaries"] = (
            capo_sagemaker.types.artifact_summaries.serialize_aws_json_1_1(
                value["artifact_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListArtifactsResponse:
    out: ListArtifactsResponse = {}  # type: ignore[typeddict-item]
    if "ArtifactSummaries" in data:
        import capo_sagemaker.types.artifact_summaries

        out["artifact_summaries"] = (
            capo_sagemaker.types.artifact_summaries.deserialize_aws_json_1_1(
                data["ArtifactSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
