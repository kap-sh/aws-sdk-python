"""Generated from Smithy shape ``com.amazonaws.apigateway#PutGatewayResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.gateway_response_type
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.status_code
    import capo_api_gateway.types.string


class PutGatewayResponseRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    response_type: "capo_api_gateway.types.gateway_response_type.GatewayResponseType"
    """<p>The response type of the associated GatewayResponse</p>"""
    status_code: NotRequired["capo_api_gateway.types.status_code.StatusCode"]
    """<p>The HTTP status code of the GatewayResponse.</p>"""
    response_parameters: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>Response parameters (paths, query strings and headers) of the GatewayResponse as a string-to-string map of key-value pairs.</p>"""
    response_templates: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>Response templates of the GatewayResponse as a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutGatewayResponseRequest) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "response_parameters" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["responseParameters"] = (
            capo_api_gateway.types.map_of_string_to_string.serialize_json(
                value["response_parameters"]
            )
        )
    if "response_templates" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["responseTemplates"] = (
            capo_api_gateway.types.map_of_string_to_string.serialize_json(
                value["response_templates"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutGatewayResponseRequest:
    out: PutGatewayResponseRequest = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    if "responseParameters" in data:
        import capo_api_gateway.types.map_of_string_to_string

        out["response_parameters"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["responseParameters"]
            )
        )
    if "responseTemplates" in data:
        import capo_api_gateway.types.map_of_string_to_string

        out["response_templates"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["responseTemplates"]
            )
        )
    return out
