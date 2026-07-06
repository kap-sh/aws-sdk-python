"""Generated from Smithy shape ``com.amazonaws.glue#GetJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean_value
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.name_string


class GetJobRunRequest(TypedDict, closed=True):
    job_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Name of the job definition being run.</p>"""
    run_id: "aws_sdk_glue.types.id_string.IdString"
    """<p>The ID of the job run.</p>"""
    predecessors_included: "aws_sdk_glue.types.boolean_value.BooleanValue"
    """<p>True if a list of predecessor runs should be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobRunRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    out["RunId"] = value["run_id"]
    out["PredecessorsIncluded"] = value.get("predecessors_included", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobRunRequest:
    out: GetJobRunRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("GetJobRunRequest.job_name required")
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("GetJobRunRequest.run_id required")
    if "PredecessorsIncluded" in data:
        out["predecessors_included"] = data["PredecessorsIncluded"]
    else:
        out["predecessors_included"] = False
    return out
