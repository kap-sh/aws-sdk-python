"""Generated from Smithy shape ``com.amazonaws.glue#StartWorkflowRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.workflow_run_properties


class StartWorkflowRunRequest(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the workflow to start.</p>"""
    run_properties: NotRequired[
        "aws_sdk_glue.types.workflow_run_properties.WorkflowRunProperties"
    ]
    """<p>The workflow run properties for the new workflow run.</p> <p>Run properties may be logged. Do not pass plaintext secrets as properties. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to use them within the workflow run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkflowRunRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "run_properties" in value:
        import aws_sdk_glue.types.workflow_run_properties

        out["RunProperties"] = (
            aws_sdk_glue.types.workflow_run_properties.serialize_aws_json_1_1(
                value["run_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartWorkflowRunRequest:
    out: StartWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartWorkflowRunRequest.name required")
    if "RunProperties" in data:
        import aws_sdk_glue.types.workflow_run_properties

        out["run_properties"] = (
            aws_sdk_glue.types.workflow_run_properties.deserialize_aws_json_1_1(
                data["RunProperties"]
            )
        )
    return out
