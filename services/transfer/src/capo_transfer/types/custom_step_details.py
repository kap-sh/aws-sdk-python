"""Generated from Smithy shape ``com.amazonaws.transfer#CustomStepDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.custom_step_target
    import capo_transfer.types.custom_step_timeout_seconds
    import capo_transfer.types.source_file_location
    import capo_transfer.types.workflow_step_name


class CustomStepDetails(TypedDict, closed=True):
    name: NotRequired["capo_transfer.types.workflow_step_name.WorkflowStepName"]
    """<p>The name of the step, used as an identifier.</p>"""
    target: NotRequired["capo_transfer.types.custom_step_target.CustomStepTarget"]
    """<p>The ARN for the Lambda function that is being called.</p>"""
    timeout_seconds: NotRequired[
        "capo_transfer.types.custom_step_timeout_seconds.CustomStepTimeoutSeconds"
    ]
    """<p>Timeout, in seconds, for the step.</p>"""
    source_file_location: NotRequired[
        "capo_transfer.types.source_file_location.SourceFileLocation"
    ]
    """<p>Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.</p> <ul> <li> <p>To use the previous file as the input, enter <code>${previous.file}</code>. In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.</p> </li> <li> <p>To use the originally uploaded file location as input for this step, enter <code>${original.file}</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomStepDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "target" in value:
        out["Target"] = value["target"]
    if "timeout_seconds" in value:
        out["TimeoutSeconds"] = value["timeout_seconds"]
    if "source_file_location" in value:
        out["SourceFileLocation"] = value["source_file_location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomStepDetails:
    out: CustomStepDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Target" in data:
        out["target"] = data["Target"]
    if "TimeoutSeconds" in data:
        out["timeout_seconds"] = data["TimeoutSeconds"]
    if "SourceFileLocation" in data:
        out["source_file_location"] = data["SourceFileLocation"]
    return out
