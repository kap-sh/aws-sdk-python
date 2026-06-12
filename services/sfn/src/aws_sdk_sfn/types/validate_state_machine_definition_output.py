"""Generated from Smithy shape ``com.amazonaws.sfn#ValidateStateMachineDefinitionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.validate_state_machine_definition_diagnostic_list
    import aws_sdk_sfn.types.validate_state_machine_definition_result_code
    import aws_sdk_sfn.types.validate_state_machine_definition_truncated


class ValidateStateMachineDefinitionOutput(TypedDict):
    result: "aws_sdk_sfn.types.validate_state_machine_definition_result_code.ValidateStateMachineDefinitionResultCode"
    """<p>The result value will be <code>OK</code> when no syntax errors are found, or <code>FAIL</code> if the workflow definition does not pass verification.</p>"""
    diagnostics: "aws_sdk_sfn.types.validate_state_machine_definition_diagnostic_list.ValidateStateMachineDefinitionDiagnosticList"
    """<p>An array of diagnostic errors and warnings found during validation of the state machine definition. Since <b>warnings</b> do not prevent deploying your workflow definition, the <b>result</b> value could be <code>OK</code> even when warning diagnostics are present in the response.</p>"""
    truncated: NotRequired[
        "aws_sdk_sfn.types.validate_state_machine_definition_truncated.ValidateStateMachineDefinitionTruncated"
    ]
    """<p>The result value will be <code>true</code> if the number of diagnostics found in the workflow definition exceeds <code>maxResults</code>. When all diagnostics results are returned, the value will be <code>false</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidateStateMachineDefinitionOutput) -> dict:
    out: dict = {}
    import aws_sdk_sfn.types.validate_state_machine_definition_result_code

    out["result"] = (
        aws_sdk_sfn.types.validate_state_machine_definition_result_code.serialize_aws_json_1_0(
            value["result"]
        )
    )
    import aws_sdk_sfn.types.validate_state_machine_definition_diagnostic_list

    out["diagnostics"] = (
        aws_sdk_sfn.types.validate_state_machine_definition_diagnostic_list.serialize_aws_json_1_0(
            value["diagnostics"]
        )
    )
    if "truncated" in value:
        out["truncated"] = value["truncated"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidateStateMachineDefinitionOutput:
    out: ValidateStateMachineDefinitionOutput = {}  # type: ignore[typeddict-item]
    if "result" in data:
        import aws_sdk_sfn.types.validate_state_machine_definition_result_code

        out["result"] = (
            aws_sdk_sfn.types.validate_state_machine_definition_result_code.deserialize_aws_json_1_0(
                data["result"]
            )
        )
    else:
        raise DeserializationError(
            "ValidateStateMachineDefinitionOutput.result required"
        )
    if "diagnostics" in data:
        import aws_sdk_sfn.types.validate_state_machine_definition_diagnostic_list

        out["diagnostics"] = (
            aws_sdk_sfn.types.validate_state_machine_definition_diagnostic_list.deserialize_aws_json_1_0(
                data["diagnostics"]
            )
        )
    else:
        raise DeserializationError(
            "ValidateStateMachineDefinitionOutput.diagnostics required"
        )
    if "truncated" in data:
        out["truncated"] = data["truncated"]
    return out
