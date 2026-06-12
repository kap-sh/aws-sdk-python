"""Generated from Smithy shape ``com.amazonaws.rekognition#ListMediaAnalysisJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.extended_pagination_token
    import aws_sdk_rekognition.types.media_analysis_job_descriptions


class ListMediaAnalysisJobsResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>Pagination token, if the previous response was incomplete.</p>"""
    media_analysis_jobs: "aws_sdk_rekognition.types.media_analysis_job_descriptions.MediaAnalysisJobDescriptions"
    """<p>Contains a list of all media analysis jobs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMediaAnalysisJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_rekognition.types.media_analysis_job_descriptions

    out["MediaAnalysisJobs"] = (
        aws_sdk_rekognition.types.media_analysis_job_descriptions.serialize_aws_json_1_1(
            value["media_analysis_jobs"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMediaAnalysisJobsResponse:
    out: ListMediaAnalysisJobsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MediaAnalysisJobs" in data:
        import aws_sdk_rekognition.types.media_analysis_job_descriptions

        out["media_analysis_jobs"] = (
            aws_sdk_rekognition.types.media_analysis_job_descriptions.deserialize_aws_json_1_1(
                data["MediaAnalysisJobs"]
            )
        )
    else:
        raise DeserializationError(
            "ListMediaAnalysisJobsResponse.media_analysis_jobs required"
        )
    return out
