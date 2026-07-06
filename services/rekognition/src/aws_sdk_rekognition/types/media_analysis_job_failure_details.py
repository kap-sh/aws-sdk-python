"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisJobFailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.media_analysis_job_failure_code
    import aws_sdk_rekognition.types.string


class MediaAnalysisJobFailureDetails(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_rekognition.types.media_analysis_job_failure_code.MediaAnalysisJobFailureCode"
    ]
    """<p>Error code for the failed job.</p>"""
    message: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>Human readable error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisJobFailureDetails) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_rekognition.types.media_analysis_job_failure_code

        out["Code"] = (
            aws_sdk_rekognition.types.media_analysis_job_failure_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MediaAnalysisJobFailureDetails:
    out: MediaAnalysisJobFailureDetails = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_rekognition.types.media_analysis_job_failure_code

        out["code"] = (
            aws_sdk_rekognition.types.media_analysis_job_failure_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
