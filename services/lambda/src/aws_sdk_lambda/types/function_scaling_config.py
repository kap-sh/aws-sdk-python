"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionScalingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_scaling_config_execution_environments


class FunctionScalingConfig(TypedDict):
    min_execution_environments: NotRequired[
        "aws_sdk_lambda.types.function_scaling_config_execution_environments.FunctionScalingConfigExecutionEnvironments"
    ]
    """<p>The minimum number of execution environments to maintain for the function.</p>"""
    max_execution_environments: NotRequired[
        "aws_sdk_lambda.types.function_scaling_config_execution_environments.FunctionScalingConfigExecutionEnvironments"
    ]
    """<p>The maximum number of execution environments that can be provisioned for the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionScalingConfig) -> dict:
    out: dict = {}
    if "min_execution_environments" in value:
        out["MinExecutionEnvironments"] = value["min_execution_environments"]
    if "max_execution_environments" in value:
        out["MaxExecutionEnvironments"] = value["max_execution_environments"]
    return out


def deserialize_json(data: dict) -> FunctionScalingConfig:
    out: FunctionScalingConfig = {}  # type: ignore[typeddict-item]
    if "MinExecutionEnvironments" in data:
        out["min_execution_environments"] = data["MinExecutionEnvironments"]
    if "MaxExecutionEnvironments" in data:
        out["max_execution_environments"] = data["MaxExecutionEnvironments"]
    return out
