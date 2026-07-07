"""Generated from Smithy shape ``com.amazonaws.apigateway#DeploymentCanarySettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.boolean
    import aws_sdk_api_gateway.types.double
    import aws_sdk_api_gateway.types.map_of_string_to_string


class DeploymentCanarySettings(TypedDict, closed=True):
    percent_traffic: "aws_sdk_api_gateway.types.double.Double"
    """<p>The percentage (0.0-100.0) of traffic routed to the canary deployment.</p>"""
    stage_variable_overrides: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A stage variable overrides used for the canary release deployment. They can override existing stage variables or add new stage variables for the canary release deployment. These stage variables are represented as a string-to-string map between stage variable names and their values.</p>"""
    use_stage_cache: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>A Boolean flag to indicate whether the canary release deployment uses the stage cache or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentCanarySettings) -> dict:
    out: dict = {}
    out["percentTraffic"] = value.get("percent_traffic", 0)
    if "stage_variable_overrides" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["stageVariableOverrides"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
                value["stage_variable_overrides"]
            )
        )
    out["useStageCache"] = value.get("use_stage_cache", False)
    return out


def deserialize_json(data: dict) -> DeploymentCanarySettings:
    out: DeploymentCanarySettings = {}  # type: ignore[typeddict-item]
    if "percentTraffic" in data:
        out["percent_traffic"] = data["percentTraffic"]
    else:
        out["percent_traffic"] = 0
    if "stageVariableOverrides" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["stage_variable_overrides"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["stageVariableOverrides"]
            )
        )
    if "useStageCache" in data:
        out["use_stage_cache"] = data["useStageCache"]
    else:
        out["use_stage_cache"] = False
    return out
