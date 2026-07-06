"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_lambda_function_environment_error
    import aws_sdk_securityhub.types.field_map


class AwsLambdaFunctionEnvironment(TypedDict, closed=True):
    variables: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p>Environment variable key-value pairs.</p>"""
    error: NotRequired[
        "aws_sdk_securityhub.types.aws_lambda_function_environment_error.AwsLambdaFunctionEnvironmentError"
    ]
    """<p>An <code>AwsLambdaFunctionEnvironmentError</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionEnvironment) -> dict:
    out: dict = {}
    if "variables" in value:
        import aws_sdk_securityhub.types.field_map

        out["Variables"] = aws_sdk_securityhub.types.field_map.serialize_json(
            value["variables"]
        )
    if "error" in value:
        import aws_sdk_securityhub.types.aws_lambda_function_environment_error

        out["Error"] = (
            aws_sdk_securityhub.types.aws_lambda_function_environment_error.serialize_json(
                value["error"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionEnvironment:
    out: AwsLambdaFunctionEnvironment = {}  # type: ignore[typeddict-item]
    if "Variables" in data:
        import aws_sdk_securityhub.types.field_map

        out["variables"] = aws_sdk_securityhub.types.field_map.deserialize_json(
            data["Variables"]
        )
    if "Error" in data:
        import aws_sdk_securityhub.types.aws_lambda_function_environment_error

        out["error"] = (
            aws_sdk_securityhub.types.aws_lambda_function_environment_error.deserialize_json(
                data["Error"]
            )
        )
    return out
