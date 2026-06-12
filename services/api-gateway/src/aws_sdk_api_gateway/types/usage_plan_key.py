"""Generated from Smithy shape ``com.amazonaws.apigateway#UsagePlanKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class UsagePlanKey(TypedDict):
    id: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The Id of a usage plan key.</p>"""
    type: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The type of a usage plan key. Currently, the valid key type is <code>API_KEY</code>.</p>"""
    value: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The value of a usage plan key.</p>"""
    name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The name of a usage plan key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsagePlanKey) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        out["type"] = value["type"]
    if "value" in value:
        out["value"] = value["value"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UsagePlanKey:
    out: UsagePlanKey = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        out["type"] = data["type"]
    if "value" in data:
        out["value"] = data["value"]
    if "name" in data:
        out["name"] = data["name"]
    return out
