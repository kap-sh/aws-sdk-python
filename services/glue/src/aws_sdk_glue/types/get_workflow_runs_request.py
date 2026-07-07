"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.page_size


class GetWorkflowRunsRequest(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Name of the workflow whose metadata of runs should be returned.</p>"""
    include_graph: NotRequired["aws_sdk_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to include the workflow graph in response or not.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The maximum size of the response.</p>"""
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum number of workflow runs to be included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRunsRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "include_graph" in value:
        out["IncludeGraph"] = value["include_graph"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRunsRequest:
    out: GetWorkflowRunsRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetWorkflowRunsRequest.name required")
    if "IncludeGraph" in data:
        out["include_graph"] = data["IncludeGraph"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
