"""Generated from Smithy shape ``com.amazonaws.apigateway#PutMethodResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.map_of_string_to_boolean
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.status_code
    import capo_api_gateway.types.string


class PutMethodResponseRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "capo_api_gateway.types.string.String"
    """<p>The Resource identifier for the Method resource.</p>"""
    http_method: "capo_api_gateway.types.string.String"
    """<p>The HTTP verb of the Method resource.</p>"""
    status_code: "capo_api_gateway.types.status_code.StatusCode"
    """<p>The method response's status code.</p>"""
    response_parameters: NotRequired[
        "capo_api_gateway.types.map_of_string_to_boolean.MapOfStringToBoolean"
    ]
    """<p>A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header name and the associated value is a Boolean flag indicating whether the method response parameter is required or not. The method response header names must match the pattern of <code>method.response.header.{name}</code>, where <code>name</code> is a valid and unique header name. The response parameter names defined here are available in the integration response to be mapped from an integration response header expressed in <code>integration.response.header.{name}</code>, a static value enclosed within a pair of single quotes (e.g., <code>'application/json'</code>), or a JSON expression from the back-end response payload in the form of <code>integration.response.body.{JSON-expression}</code>, where <code>JSON-expression</code> is a valid JSON expression without the <code>$</code> prefix.)</p>"""
    response_models: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>Specifies the Model resources used for the response's content type. Response models are represented as a key/value map, with a content type as the key and a Model name as the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutMethodResponseRequest) -> dict:
    out: dict = {}
    if "response_parameters" in value:
        import capo_api_gateway.types.map_of_string_to_boolean

        out["responseParameters"] = (
            capo_api_gateway.types.map_of_string_to_boolean.serialize_json(
                value["response_parameters"]
            )
        )
    if "response_models" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["responseModels"] = (
            capo_api_gateway.types.map_of_string_to_string.serialize_json(
                value["response_models"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutMethodResponseRequest:
    out: PutMethodResponseRequest = {}  # type: ignore[typeddict-item]
    if "responseParameters" in data:
        import capo_api_gateway.types.map_of_string_to_boolean

        out["response_parameters"] = (
            capo_api_gateway.types.map_of_string_to_boolean.deserialize_json(
                data["responseParameters"]
            )
        )
    if "responseModels" in data:
        import capo_api_gateway.types.map_of_string_to_string

        out["response_models"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["responseModels"]
            )
        )
    return out
