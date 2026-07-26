"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiStage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.map_of_api_stage_throttle_settings
    import capo_api_gateway.types.string


class ApiStage(TypedDict, closed=True):
    api_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>API Id of the associated API stage in a usage plan.</p>"""
    stage: NotRequired["capo_api_gateway.types.string.String"]
    """<p>API stage name of the associated API stage in a usage plan.</p>"""
    throttle: NotRequired[
        "capo_api_gateway.types.map_of_api_stage_throttle_settings.MapOfApiStageThrottleSettings"
    ]
    """<p>Map containing method level throttling information for API stage in a usage plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiStage) -> dict:
    out: dict = {}
    if "api_id" in value:
        out["apiId"] = value["api_id"]
    if "stage" in value:
        out["stage"] = value["stage"]
    if "throttle" in value:
        import capo_api_gateway.types.map_of_api_stage_throttle_settings

        out["throttle"] = (
            capo_api_gateway.types.map_of_api_stage_throttle_settings.serialize_json(
                value["throttle"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApiStage:
    out: ApiStage = {}  # type: ignore[typeddict-item]
    if "apiId" in data:
        out["api_id"] = data["apiId"]
    if "stage" in data:
        out["stage"] = data["stage"]
    if "throttle" in data:
        import capo_api_gateway.types.map_of_api_stage_throttle_settings

        out["throttle"] = (
            capo_api_gateway.types.map_of_api_stage_throttle_settings.deserialize_json(
                data["throttle"]
            )
        )
    return out
