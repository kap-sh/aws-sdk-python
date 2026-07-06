"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetJobDetailsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.job_details


class GetJobDetailsOutput(TypedDict, closed=True):
    job_details: NotRequired["aws_sdk_codepipeline.types.job_details.JobDetails"]
    """<p>The details of the job.</p> <note> <p>If AWSSessionCredentials is used, a long-running job can call <code>GetJobDetails</code> again to obtain new credentials.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobDetailsOutput) -> dict:
    out: dict = {}
    if "job_details" in value:
        import aws_sdk_codepipeline.types.job_details

        out["jobDetails"] = (
            aws_sdk_codepipeline.types.job_details.serialize_aws_json_1_1(
                value["job_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobDetailsOutput:
    out: GetJobDetailsOutput = {}  # type: ignore[typeddict-item]
    if "jobDetails" in data:
        import aws_sdk_codepipeline.types.job_details

        out["job_details"] = (
            aws_sdk_codepipeline.types.job_details.deserialize_aws_json_1_1(
                data["jobDetails"]
            )
        )
    return out
