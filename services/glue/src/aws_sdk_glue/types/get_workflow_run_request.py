"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_boolean


class GetWorkflowRunRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Name of the workflow being run.</p>"""
    run_id: "aws_sdk_glue.types.id_string.IdString"
    """<p>The ID of the workflow run.</p>"""
    include_graph: NotRequired["aws_sdk_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to include the workflow graph in response or not.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRunRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RunId"] = value["run_id"]
    if "include_graph" in value:
        out["IncludeGraph"] = value["include_graph"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRunRequest:
    out: GetWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetWorkflowRunRequest.name required")
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("GetWorkflowRunRequest.run_id required")
    if "IncludeGraph" in data:
        out["include_graph"] = data["IncludeGraph"]
    return out
