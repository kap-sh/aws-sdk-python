"""Generated from Smithy shape ``com.amazonaws.lambda#EnvironmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.environment_error
    import aws_sdk_lambda.types.environment_variables


class EnvironmentResponse(TypedDict):
    variables: NotRequired[
        "aws_sdk_lambda.types.environment_variables.EnvironmentVariables"
    ]
    """<p>Environment variable key-value pairs. Omitted from CloudTrail logs.</p>"""
    error: NotRequired["aws_sdk_lambda.types.environment_error.EnvironmentError"]
    """<p>Error messages for environment variables that couldn't be applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentResponse) -> dict:
    out: dict = {}
    if "variables" in value:
        import aws_sdk_lambda.types.environment_variables

        out["Variables"] = aws_sdk_lambda.types.environment_variables.serialize_json(
            value["variables"]
        )
    if "error" in value:
        import aws_sdk_lambda.types.environment_error

        out["Error"] = aws_sdk_lambda.types.environment_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> EnvironmentResponse:
    out: EnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "Variables" in data:
        import aws_sdk_lambda.types.environment_variables

        out["variables"] = aws_sdk_lambda.types.environment_variables.deserialize_json(
            data["Variables"]
        )
    if "Error" in data:
        import aws_sdk_lambda.types.environment_error

        out["error"] = aws_sdk_lambda.types.environment_error.deserialize_json(
            data["Error"]
        )
    return out
