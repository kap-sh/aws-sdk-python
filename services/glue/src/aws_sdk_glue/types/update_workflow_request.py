"""Generated from Smithy shape ``com.amazonaws.glue#UpdateWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.workflow_description_string
    import aws_sdk_glue.types.workflow_run_properties


class UpdateWorkflowRequest(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Name of the workflow to be updated.</p>"""
    description: NotRequired[
        "aws_sdk_glue.types.workflow_description_string.WorkflowDescriptionString"
    ]
    """<p>The description of the workflow.</p>"""
    default_run_properties: NotRequired[
        "aws_sdk_glue.types.workflow_run_properties.WorkflowRunProperties"
    ]
    """<p>A collection of properties to be used as part of each execution of the workflow.</p> <p>Run properties may be logged. Do not pass plaintext secrets as properties. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to use them within the workflow run.</p>"""
    max_concurrent_runs: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkflowRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "default_run_properties" in value:
        import aws_sdk_glue.types.workflow_run_properties

        out["DefaultRunProperties"] = (
            aws_sdk_glue.types.workflow_run_properties.serialize_aws_json_1_1(
                value["default_run_properties"]
            )
        )
    if "max_concurrent_runs" in value:
        out["MaxConcurrentRuns"] = value["max_concurrent_runs"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkflowRequest:
    out: UpdateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateWorkflowRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "DefaultRunProperties" in data:
        import aws_sdk_glue.types.workflow_run_properties

        out["default_run_properties"] = (
            aws_sdk_glue.types.workflow_run_properties.deserialize_aws_json_1_1(
                data["DefaultRunProperties"]
            )
        )
    if "MaxConcurrentRuns" in data:
        out["max_concurrent_runs"] = data["MaxConcurrentRuns"]
    return out
