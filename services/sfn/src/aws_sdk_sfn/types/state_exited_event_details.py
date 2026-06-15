"""Generated from Smithy shape ``com.amazonaws.sfn#StateExitedEventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.assigned_variables
    import aws_sdk_sfn.types.assigned_variables_details
    import aws_sdk_sfn.types.history_event_execution_data_details
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.sensitive_data


class StateExitedEventDetails(TypedDict):
    name: "aws_sdk_sfn.types.name.Name"
    r"""<p>The name of the state.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>\" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    output: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON output data of the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    output_details: NotRequired[
        "aws_sdk_sfn.types.history_event_execution_data_details.HistoryEventExecutionDataDetails"
    ]
    """<p>Contains details about the output of an execution history event.</p>"""
    assigned_variables: NotRequired[
        "aws_sdk_sfn.types.assigned_variables.AssignedVariables"
    ]
    """<p>Map of variable name and value as a serialized JSON representation.</p>"""
    assigned_variables_details: NotRequired[
        "aws_sdk_sfn.types.assigned_variables_details.AssignedVariablesDetails"
    ]
    """<p>Provides details about input or output in an execution history event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateExitedEventDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "output" in value:
        out["output"] = value["output"]
    if "output_details" in value:
        import aws_sdk_sfn.types.history_event_execution_data_details

        out["outputDetails"] = (
            aws_sdk_sfn.types.history_event_execution_data_details.serialize_aws_json_1_0(
                value["output_details"]
            )
        )
    if "assigned_variables" in value:
        import aws_sdk_sfn.types.assigned_variables

        out["assignedVariables"] = (
            aws_sdk_sfn.types.assigned_variables.serialize_aws_json_1_0(
                value["assigned_variables"]
            )
        )
    if "assigned_variables_details" in value:
        import aws_sdk_sfn.types.assigned_variables_details

        out["assignedVariablesDetails"] = (
            aws_sdk_sfn.types.assigned_variables_details.serialize_aws_json_1_0(
                value["assigned_variables_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StateExitedEventDetails:
    out: StateExitedEventDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StateExitedEventDetails.name required")
    if "output" in data:
        out["output"] = data["output"]
    if "outputDetails" in data:
        import aws_sdk_sfn.types.history_event_execution_data_details

        out["output_details"] = (
            aws_sdk_sfn.types.history_event_execution_data_details.deserialize_aws_json_1_0(
                data["outputDetails"]
            )
        )
    if "assignedVariables" in data:
        import aws_sdk_sfn.types.assigned_variables

        out["assigned_variables"] = (
            aws_sdk_sfn.types.assigned_variables.deserialize_aws_json_1_0(
                data["assignedVariables"]
            )
        )
    if "assignedVariablesDetails" in data:
        import aws_sdk_sfn.types.assigned_variables_details

        out["assigned_variables_details"] = (
            aws_sdk_sfn.types.assigned_variables_details.deserialize_aws_json_1_0(
                data["assignedVariablesDetails"]
            )
        )
    return out
