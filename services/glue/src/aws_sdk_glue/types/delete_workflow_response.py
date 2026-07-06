"""Generated from Smithy shape ``com.amazonaws.glue#DeleteWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class DeleteWorkflowResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Name of the workflow specified in input.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkflowResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkflowResponse:
    out: DeleteWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
