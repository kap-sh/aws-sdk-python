"""Generated from Smithy shape ``com.amazonaws.glue#Predecessor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.name_string


class Predecessor(TypedDict, closed=True):
    job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the job definition used by the predecessor job run.</p>"""
    run_id: NotRequired["aws_sdk_glue.types.id_string.IdString"]
    """<p>The job-run ID of the predecessor job run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Predecessor) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Predecessor:
    out: Predecessor = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    return out
