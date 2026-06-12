"""Generated from Smithy shape ``com.amazonaws.sfn#MockInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.mock_error_output
    import aws_sdk_sfn.types.mock_response_validation_mode
    import aws_sdk_sfn.types.sensitive_data


class MockInput(TypedDict):
    result: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>A JSON string containing the mocked result of the state invocation.</p>"""
    error_output: NotRequired["aws_sdk_sfn.types.mock_error_output.MockErrorOutput"]
    """<p>The mocked error output when calling TestState. When specified, the mocked response is returned as a JSON object that contains an <code>error</code> and <code>cause</code> field.</p>"""
    field_validation_mode: NotRequired[
        "aws_sdk_sfn.types.mock_response_validation_mode.MockResponseValidationMode"
    ]
    """<p>Determines the level of strictness when validating mocked results against their respective API models. Values include:</p> <ul> <li> <p> <code>STRICT</code>: All required fields must be present, and all present fields must conform to the API's schema.</p> </li> <li> <p> <code>PRESENT</code>: All present fields must conform to the API's schema.</p> </li> <li> <p> <code>NONE</code>: No validation is performed.</p> </li> </ul> <p>If no value is specified, the default value is <code>STRICT</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MockInput) -> dict:
    out: dict = {}
    if "result" in value:
        out["result"] = value["result"]
    if "error_output" in value:
        import aws_sdk_sfn.types.mock_error_output

        out["errorOutput"] = aws_sdk_sfn.types.mock_error_output.serialize_aws_json_1_0(
            value["error_output"]
        )
    if "field_validation_mode" in value:
        import aws_sdk_sfn.types.mock_response_validation_mode

        out["fieldValidationMode"] = (
            aws_sdk_sfn.types.mock_response_validation_mode.serialize_aws_json_1_0(
                value["field_validation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MockInput:
    out: MockInput = {}  # type: ignore[typeddict-item]
    if "result" in data:
        out["result"] = data["result"]
    if "errorOutput" in data:
        import aws_sdk_sfn.types.mock_error_output

        out["error_output"] = (
            aws_sdk_sfn.types.mock_error_output.deserialize_aws_json_1_0(
                data["errorOutput"]
            )
        )
    if "fieldValidationMode" in data:
        import aws_sdk_sfn.types.mock_response_validation_mode

        out["field_validation_mode"] = (
            aws_sdk_sfn.types.mock_response_validation_mode.deserialize_aws_json_1_0(
                data["fieldValidationMode"]
            )
        )
    return out
