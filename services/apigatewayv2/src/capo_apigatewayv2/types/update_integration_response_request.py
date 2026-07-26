"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateIntegrationResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.content_handling_strategy
    import capo_apigatewayv2.types.integration_parameters
    import capo_apigatewayv2.types.selection_expression
    import capo_apigatewayv2.types.selection_key
    import capo_apigatewayv2.types.template_map


class UpdateIntegrationResponseRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    content_handling_strategy: NotRequired[
        "capo_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
    ]
    """<p>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>"""
    integration_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The integration ID.</p>"""
    integration_response_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The integration response ID.</p>"""
    integration_response_key: NotRequired[
        "capo_apigatewayv2.types.selection_key.SelectionKey"
    ]
    """<p>The integration response key.</p>"""
    response_parameters: NotRequired[
        "capo_apigatewayv2.types.integration_parameters.IntegrationParameters"
    ]
    """<p>A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.<replaceable>{name}</replaceable> , where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.<replaceable>{name}</replaceable> or integration.response.body.<replaceable>{JSON-expression}</replaceable> , where <replaceable>{name}</replaceable> is a valid and unique response header name and <replaceable>{JSON-expression}</replaceable> is a valid JSON expression without the $ prefix.</p>"""
    response_templates: NotRequired["capo_apigatewayv2.types.template_map.TemplateMap"]
    """<p>The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.</p>"""
    template_selection_expression: NotRequired[
        "capo_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The template selection expression for the integration response. Supported only for WebSocket APIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegrationResponseRequest) -> dict:
    out: dict = {}
    if "content_handling_strategy" in value:
        import capo_apigatewayv2.types.content_handling_strategy

        out["contentHandlingStrategy"] = (
            capo_apigatewayv2.types.content_handling_strategy.serialize_json(
                value["content_handling_strategy"]
            )
        )
    if "integration_response_key" in value:
        out["integrationResponseKey"] = value["integration_response_key"]
    if "response_parameters" in value:
        import capo_apigatewayv2.types.integration_parameters

        out["responseParameters"] = (
            capo_apigatewayv2.types.integration_parameters.serialize_json(
                value["response_parameters"]
            )
        )
    if "response_templates" in value:
        import capo_apigatewayv2.types.template_map

        out["responseTemplates"] = capo_apigatewayv2.types.template_map.serialize_json(
            value["response_templates"]
        )
    if "template_selection_expression" in value:
        out["templateSelectionExpression"] = value["template_selection_expression"]
    return out


def deserialize_json(data: dict) -> UpdateIntegrationResponseRequest:
    out: UpdateIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
    if "contentHandlingStrategy" in data:
        import capo_apigatewayv2.types.content_handling_strategy

        out["content_handling_strategy"] = (
            capo_apigatewayv2.types.content_handling_strategy.deserialize_json(
                data["contentHandlingStrategy"]
            )
        )
    if "integrationResponseKey" in data:
        out["integration_response_key"] = data["integrationResponseKey"]
    if "responseParameters" in data:
        import capo_apigatewayv2.types.integration_parameters

        out["response_parameters"] = (
            capo_apigatewayv2.types.integration_parameters.deserialize_json(
                data["responseParameters"]
            )
        )
    if "responseTemplates" in data:
        import capo_apigatewayv2.types.template_map

        out["response_templates"] = (
            capo_apigatewayv2.types.template_map.deserialize_json(
                data["responseTemplates"]
            )
        )
    if "templateSelectionExpression" in data:
        out["template_selection_expression"] = data["templateSelectionExpression"]
    return out
