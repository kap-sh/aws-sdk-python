"""Generated from Smithy shape ``com.amazonaws.lambda#PutFunctionScalingConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_scaling_config
    import capo_lambda.types.published_function_qualifier
    import capo_lambda.types.unqualified_function_name


class PutFunctionScalingConfigRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName"
    """<p>The name or ARN of the Lambda function.</p>"""
    qualifier: (
        "capo_lambda.types.published_function_qualifier.PublishedFunctionQualifier"
    )
    """<p>Specify a version or alias to set the scaling configuration for a published version of the function.</p>"""
    function_scaling_config: NotRequired[
        "capo_lambda.types.function_scaling_config.FunctionScalingConfig"
    ]
    """<p>The scaling configuration to apply to the function, including minimum and maximum execution environment limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionScalingConfigRequest) -> dict:
    out: dict = {}
    if "function_scaling_config" in value:
        import capo_lambda.types.function_scaling_config

        out["FunctionScalingConfig"] = (
            capo_lambda.types.function_scaling_config.serialize_json(
                value["function_scaling_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutFunctionScalingConfigRequest:
    out: PutFunctionScalingConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("FunctionScalingConfig") is not None:
        import capo_lambda.types.function_scaling_config

        out["function_scaling_config"] = (
            capo_lambda.types.function_scaling_config.deserialize_json(
                data["FunctionScalingConfig"]
            )
        )
    return out
