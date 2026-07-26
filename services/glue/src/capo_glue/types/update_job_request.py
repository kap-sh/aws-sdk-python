"""Generated from Smithy shape ``com.amazonaws.glue#UpdateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.job_update
    import capo_glue.types.name_string


class UpdateJobRequest(TypedDict, closed=True):
    job_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the job definition to update.</p>"""
    job_update: "capo_glue.types.job_update.JobUpdate"
    """<p>Specifies the values with which to update the job definition. Unspecified configuration is removed or reset to default values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJobRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    import capo_glue.types.job_update

    out["JobUpdate"] = capo_glue.types.job_update.serialize_aws_json_1_1(
        value["job_update"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJobRequest:
    out: UpdateJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("UpdateJobRequest.job_name required")
    if "JobUpdate" in data:
        import capo_glue.types.job_update

        out["job_update"] = capo_glue.types.job_update.deserialize_aws_json_1_1(
            data["JobUpdate"]
        )
    else:
        raise DeserializationError("UpdateJobRequest.job_update required")
    return out
