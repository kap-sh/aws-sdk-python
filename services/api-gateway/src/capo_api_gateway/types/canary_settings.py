"""Generated from Smithy shape ``com.amazonaws.apigateway#CanarySettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.double
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string


class CanarySettings(TypedDict, closed=True):
    percent_traffic: "capo_api_gateway.types.double.Double"
    """<p>The percent (0-100) of traffic diverted to a canary deployment.</p>"""
    deployment_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The ID of the canary deployment.</p>"""
    stage_variable_overrides: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>Stage variables overridden for a canary release deployment, including new stage variables introduced in the canary. These stage variables are represented as a string-to-string map between stage variable names and their values.</p>"""
    use_stage_cache: "capo_api_gateway.types.boolean.Boolean"
    """<p>A Boolean flag to indicate whether the canary deployment uses the stage cache or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanarySettings) -> dict:
    out: dict = {}
    out["percentTraffic"] = value.get("percent_traffic", 0)
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "stage_variable_overrides" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["stageVariableOverrides"] = (
            capo_api_gateway.types.map_of_string_to_string.serialize_json(
                value["stage_variable_overrides"]
            )
        )
    out["useStageCache"] = value.get("use_stage_cache", False)
    return out


def deserialize_json(data: dict) -> CanarySettings:
    out: CanarySettings = {}  # type: ignore[typeddict-item]
    if "percentTraffic" in data:
        out["percent_traffic"] = data["percentTraffic"]
    else:
        out["percent_traffic"] = 0
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "stageVariableOverrides" in data:
        import capo_api_gateway.types.map_of_string_to_string

        out["stage_variable_overrides"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["stageVariableOverrides"]
            )
        )
    if "useStageCache" in data:
        out["use_stage_cache"] = data["useStageCache"]
    else:
        out["use_stage_cache"] = False
    return out
