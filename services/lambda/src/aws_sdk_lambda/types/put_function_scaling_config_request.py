"""Generated from Smithy shape ``com.amazonaws.lambda#PutFunctionScalingConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_scaling_config
    import aws_sdk_lambda.types.published_function_qualifier
    import aws_sdk_lambda.types.unqualified_function_name


class PutFunctionScalingConfigRequest(TypedDict):
    function_name: (
        "aws_sdk_lambda.types.unqualified_function_name.UnqualifiedFunctionName"
    )
    """<p>The name or ARN of the Lambda function.</p>"""
    qualifier: (
        "aws_sdk_lambda.types.published_function_qualifier.PublishedFunctionQualifier"
    )
    """<p>Specify a version or alias to set the scaling configuration for a published version of the function.</p>"""
    function_scaling_config: NotRequired[
        "aws_sdk_lambda.types.function_scaling_config.FunctionScalingConfig"
    ]
    """<p>The scaling configuration to apply to the function, including minimum and maximum execution environment limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionScalingConfigRequest) -> dict:
    out: dict = {}
    if "function_scaling_config" in value:
        import aws_sdk_lambda.types.function_scaling_config

        out["FunctionScalingConfig"] = (
            aws_sdk_lambda.types.function_scaling_config.serialize_json(
                value["function_scaling_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutFunctionScalingConfigRequest:
    out: PutFunctionScalingConfigRequest = {}  # type: ignore[typeddict-item]
    if "FunctionScalingConfig" in data:
        import aws_sdk_lambda.types.function_scaling_config

        out["function_scaling_config"] = (
            aws_sdk_lambda.types.function_scaling_config.deserialize_json(
                data["FunctionScalingConfig"]
            )
        )
    return out
