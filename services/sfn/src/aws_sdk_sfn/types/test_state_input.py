"""Generated from Smithy shape ``com.amazonaws.sfn#TestStateInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.definition
    import aws_sdk_sfn.types.inspection_level
    import aws_sdk_sfn.types.mock_input
    import aws_sdk_sfn.types.reveal_secrets
    import aws_sdk_sfn.types.sensitive_data
    import aws_sdk_sfn.types.test_state_configuration
    import aws_sdk_sfn.types.test_state_state_name


class TestStateInput(TypedDict):
    definition: "aws_sdk_sfn.types.definition.Definition"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html\">Amazon States Language</a> (ASL) definition of the state or state machine.</p>"""
    role_arn: NotRequired["aws_sdk_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the execution role with the required IAM permissions for the state.</p>"""
    input: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>A string that contains the JSON input data for the state.</p>"""
    inspection_level: NotRequired["aws_sdk_sfn.types.inspection_level.InspectionLevel"]
    """<p>Determines the values to return when a state is tested. You can specify one of the following types:</p> <ul> <li> <p> <code>INFO</code>: Shows the final state output. By default, Step Functions sets <code>inspectionLevel</code> to <code>INFO</code> if you don't specify a level.</p> </li> <li> <p> <code>DEBUG</code>: Shows the final state output along with the input and output data processing result.</p> </li> <li> <p> <code>TRACE</code>: Shows the HTTP request and response for an HTTP Task. This level also shows the final state output along with the input and output data processing result.</p> </li> </ul> <p>Each of these levels also provide information about the status of the state execution and the next state to transition to.</p>"""
    reveal_secrets: "aws_sdk_sfn.types.reveal_secrets.RevealSecrets"
    r"""<p>Specifies whether or not to include secret information in the test result. For HTTP Tasks, a secret includes the data that an EventBridge connection adds to modify the HTTP request headers, query parameters, and body. Step Functions doesn't omit any information included in the state definition or the HTTP response.</p> <p>If you set <code>revealSecrets</code> to <code>true</code>, you must make sure that the IAM user that calls the <code>TestState</code> API has permission for the <code>states:RevealSecrets</code> action. For an example of IAM policy that sets the <code>states:RevealSecrets</code> permission, see <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-permissions\">IAM permissions to test a state</a>. Without this permission, Step Functions throws an access denied error.</p> <p>By default, <code>revealSecrets</code> is set to <code>false</code>.</p>"""
    variables: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>JSON object literal that sets variables used in the state under test. Object keys are the variable names and values are the variable values.</p>"""
    state_name: NotRequired[
        "aws_sdk_sfn.types.test_state_state_name.TestStateStateName"
    ]
    """<p>Denotes the particular state within a state machine definition to be tested. If this field is specified, the <code>definition</code> must contain a fully-formed state machine definition.</p>"""
    mock: NotRequired["aws_sdk_sfn.types.mock_input.MockInput"]
    """<p>Defines a mocked result or error for the state under test.</p> <p>A mock can only be specified for Task, Map, or Parallel states. If it is specified for another state type, an exception will be thrown.</p>"""
    context: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>A JSON string representing a valid Context object for the state under test. This field may only be specified if a mock is specified in the same request.</p>"""
    state_configuration: NotRequired[
        "aws_sdk_sfn.types.test_state_configuration.TestStateConfiguration"
    ]
    """<p>Contains configurations for the state under test.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestStateInput) -> dict:
    out: dict = {}
    out["definition"] = value["definition"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "input" in value:
        out["input"] = value["input"]
    if "inspection_level" in value:
        import aws_sdk_sfn.types.inspection_level

        out["inspectionLevel"] = (
            aws_sdk_sfn.types.inspection_level.serialize_aws_json_1_0(
                value["inspection_level"]
            )
        )
    out["revealSecrets"] = value.get("reveal_secrets", False)
    if "variables" in value:
        out["variables"] = value["variables"]
    if "state_name" in value:
        out["stateName"] = value["state_name"]
    if "mock" in value:
        import aws_sdk_sfn.types.mock_input

        out["mock"] = aws_sdk_sfn.types.mock_input.serialize_aws_json_1_0(value["mock"])
    if "context" in value:
        out["context"] = value["context"]
    if "state_configuration" in value:
        import aws_sdk_sfn.types.test_state_configuration

        out["stateConfiguration"] = (
            aws_sdk_sfn.types.test_state_configuration.serialize_aws_json_1_0(
                value["state_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestStateInput:
    out: TestStateInput = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("TestStateInput.definition required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "input" in data:
        out["input"] = data["input"]
    if "inspectionLevel" in data:
        import aws_sdk_sfn.types.inspection_level

        out["inspection_level"] = (
            aws_sdk_sfn.types.inspection_level.deserialize_aws_json_1_0(
                data["inspectionLevel"]
            )
        )
    if "revealSecrets" in data:
        out["reveal_secrets"] = data["revealSecrets"]
    else:
        out["reveal_secrets"] = False
    if "variables" in data:
        out["variables"] = data["variables"]
    if "stateName" in data:
        out["state_name"] = data["stateName"]
    if "mock" in data:
        import aws_sdk_sfn.types.mock_input

        out["mock"] = aws_sdk_sfn.types.mock_input.deserialize_aws_json_1_0(
            data["mock"]
        )
    if "context" in data:
        out["context"] = data["context"]
    if "stateConfiguration" in data:
        import aws_sdk_sfn.types.test_state_configuration

        out["state_configuration"] = (
            aws_sdk_sfn.types.test_state_configuration.deserialize_aws_json_1_0(
                data["stateConfiguration"]
            )
        )
    return out
