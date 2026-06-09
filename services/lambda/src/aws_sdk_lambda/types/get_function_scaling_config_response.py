"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionScalingConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_arn
    import aws_sdk_lambda.types.function_scaling_config


class GetFunctionScalingConfigResponse(TypedDict):
    function_arn: NotRequired["aws_sdk_lambda.types.function_arn.FunctionArn"]
    """<p>The Amazon Resource Name (ARN) of the function.</p>"""
    applied_function_scaling_config: NotRequired[
        "aws_sdk_lambda.types.function_scaling_config.FunctionScalingConfig"
    ]
    """<p>The scaling configuration that is currently applied to the function. This represents the actual scaling settings in effect.</p>"""
    requested_function_scaling_config: NotRequired[
        "aws_sdk_lambda.types.function_scaling_config.FunctionScalingConfig"
    ]
    """<p>The scaling configuration that was requested for the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionScalingConfigResponse) -> dict:
    out: dict = {}
    if "function_arn" in value:
        out["FunctionArn"] = value["function_arn"]
    if "applied_function_scaling_config" in value:
        import aws_sdk_lambda.types.function_scaling_config

        out["AppliedFunctionScalingConfig"] = (
            aws_sdk_lambda.types.function_scaling_config.serialize_json(
                value["applied_function_scaling_config"]
            )
        )
    if "requested_function_scaling_config" in value:
        import aws_sdk_lambda.types.function_scaling_config

        out["RequestedFunctionScalingConfig"] = (
            aws_sdk_lambda.types.function_scaling_config.serialize_json(
                value["requested_function_scaling_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetFunctionScalingConfigResponse:
    out: GetFunctionScalingConfigResponse = {}  # type: ignore[typeddict-item]
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    if "AppliedFunctionScalingConfig" in data:
        import aws_sdk_lambda.types.function_scaling_config

        out["applied_function_scaling_config"] = (
            aws_sdk_lambda.types.function_scaling_config.deserialize_json(
                data["AppliedFunctionScalingConfig"]
            )
        )
    if "RequestedFunctionScalingConfig" in data:
        import aws_sdk_lambda.types.function_scaling_config

        out["requested_function_scaling_config"] = (
            aws_sdk_lambda.types.function_scaling_config.deserialize_json(
                data["RequestedFunctionScalingConfig"]
            )
        )
    return out
