"""Generated from Smithy shape ``com.amazonaws.apigateway#RequestValidator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.string


class RequestValidator(TypedDict, closed=True):
    id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier of this RequestValidator.</p>"""
    name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of this RequestValidator</p>"""
    validate_request_body: "capo_api_gateway.types.boolean.Boolean"
    """<p>A Boolean flag to indicate whether to validate a request body according to the configured Model schema.</p>"""
    validate_request_parameters: "capo_api_gateway.types.boolean.Boolean"
    """<p>A Boolean flag to indicate whether to validate request parameters (<code>true</code>) or not (<code>false</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestValidator) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    out["validateRequestBody"] = value.get("validate_request_body", False)
    out["validateRequestParameters"] = value.get("validate_request_parameters", False)
    return out


def deserialize_json(data: dict) -> RequestValidator:
    out: RequestValidator = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "validateRequestBody" in data:
        out["validate_request_body"] = data["validateRequestBody"]
    else:
        out["validate_request_body"] = False
    if "validateRequestParameters" in data:
        out["validate_request_parameters"] = data["validateRequestParameters"]
    else:
        out["validate_request_parameters"] = False
    return out
