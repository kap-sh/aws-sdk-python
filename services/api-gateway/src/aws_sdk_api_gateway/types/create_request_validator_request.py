"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateRequestValidatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.boolean
    import aws_sdk_api_gateway.types.string


class CreateRequestValidatorRequest(TypedDict, closed=True):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The name of the to-be-created RequestValidator.</p>"""
    validate_request_body: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>A Boolean flag to indicate whether to validate request body according to the configured model schema for the method (<code>true</code>) or not (<code>false</code>).</p>"""
    validate_request_parameters: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>A Boolean flag to indicate whether to validate request parameters, <code>true</code>, or not <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRequestValidatorRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["validateRequestBody"] = value.get("validate_request_body", False)
    out["validateRequestParameters"] = value.get("validate_request_parameters", False)
    return out


def deserialize_json(data: dict) -> CreateRequestValidatorRequest:
    out: CreateRequestValidatorRequest = {}  # type: ignore[typeddict-item]
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
