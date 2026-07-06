"""Generated from Smithy shape ``com.amazonaws.apigateway#StageKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class StageKey(TypedDict, closed=True):
    rest_api_id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The string identifier of the associated RestApi.</p>"""
    stage_name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The stage name associated with the stage key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StageKey) -> dict:
    out: dict = {}
    if "rest_api_id" in value:
        out["restApiId"] = value["rest_api_id"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    return out


def deserialize_json(data: dict) -> StageKey:
    out: StageKey = {}  # type: ignore[typeddict-item]
    if "restApiId" in data:
        out["rest_api_id"] = data["restApiId"]
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    return out
