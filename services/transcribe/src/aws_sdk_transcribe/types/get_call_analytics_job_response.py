"""Generated from Smithy shape ``com.amazonaws.transcribe#GetCallAnalyticsJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.call_analytics_job


class GetCallAnalyticsJobResponse(TypedDict):
    call_analytics_job: NotRequired[
        "aws_sdk_transcribe.types.call_analytics_job.CallAnalyticsJob"
    ]
    """<p>Provides detailed information about the specified Call Analytics job, including job status and, if applicable, failure reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCallAnalyticsJobResponse) -> dict:
    out: dict = {}
    if "call_analytics_job" in value:
        import aws_sdk_transcribe.types.call_analytics_job

        out["CallAnalyticsJob"] = (
            aws_sdk_transcribe.types.call_analytics_job.serialize_aws_json_1_1(
                value["call_analytics_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCallAnalyticsJobResponse:
    out: GetCallAnalyticsJobResponse = {}  # type: ignore[typeddict-item]
    if "CallAnalyticsJob" in data:
        import aws_sdk_transcribe.types.call_analytics_job

        out["call_analytics_job"] = (
            aws_sdk_transcribe.types.call_analytics_job.deserialize_aws_json_1_1(
                data["CallAnalyticsJob"]
            )
        )
    return out
