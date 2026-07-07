"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRunPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.name_string


class GetWorkflowRunPropertiesRequest(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Name of the workflow which was run.</p>"""
    run_id: "aws_sdk_glue.types.id_string.IdString"
    """<p>The ID of the workflow run whose run properties should be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRunPropertiesRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRunPropertiesRequest:
    out: GetWorkflowRunPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetWorkflowRunPropertiesRequest.name required")
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("GetWorkflowRunPropertiesRequest.run_id required")
    return out
