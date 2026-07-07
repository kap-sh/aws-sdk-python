"""Generated from Smithy shape ``com.amazonaws.codepipeline#AcknowledgeThirdPartyJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.job_status


class AcknowledgeThirdPartyJobOutput(TypedDict, closed=True):
    status: NotRequired["aws_sdk_codepipeline.types.job_status.JobStatus"]
    """<p>The status information for the third party job, if any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcknowledgeThirdPartyJobOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_codepipeline.types.job_status

        out["status"] = aws_sdk_codepipeline.types.job_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcknowledgeThirdPartyJobOutput:
    out: AcknowledgeThirdPartyJobOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_codepipeline.types.job_status

        out["status"] = aws_sdk_codepipeline.types.job_status.deserialize_aws_json_1_1(
            data["status"]
        )
    return out
