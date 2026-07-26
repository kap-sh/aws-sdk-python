"""Generated from Smithy shape ``com.amazonaws.codepipeline#AcknowledgeJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.job_status


class AcknowledgeJobOutput(TypedDict, closed=True):
    status: NotRequired["capo_codepipeline.types.job_status.JobStatus"]
    """<p>Whether the job worker has received the specified job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcknowledgeJobOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_codepipeline.types.job_status

        out["status"] = capo_codepipeline.types.job_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcknowledgeJobOutput:
    out: AcknowledgeJobOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_codepipeline.types.job_status

        out["status"] = capo_codepipeline.types.job_status.deserialize_aws_json_1_1(
            data["status"]
        )
    return out
