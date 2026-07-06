"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRunPropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.workflow_run_properties


class GetWorkflowRunPropertiesResponse(TypedDict, closed=True):
    run_properties: NotRequired[
        "aws_sdk_glue.types.workflow_run_properties.WorkflowRunProperties"
    ]
    """<p>The workflow run properties which were set during the specified run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRunPropertiesResponse) -> dict:
    out: dict = {}
    if "run_properties" in value:
        import aws_sdk_glue.types.workflow_run_properties

        out["RunProperties"] = (
            aws_sdk_glue.types.workflow_run_properties.serialize_aws_json_1_1(
                value["run_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRunPropertiesResponse:
    out: GetWorkflowRunPropertiesResponse = {}  # type: ignore[typeddict-item]
    if "RunProperties" in data:
        import aws_sdk_glue.types.workflow_run_properties

        out["run_properties"] = (
            aws_sdk_glue.types.workflow_run_properties.deserialize_aws_json_1_1(
                data["RunProperties"]
            )
        )
    return out
