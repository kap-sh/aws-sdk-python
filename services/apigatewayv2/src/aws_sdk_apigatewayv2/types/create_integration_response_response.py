"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateIntegrationResponseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.content_handling_strategy
    import aws_sdk_apigatewayv2.types.id
    import aws_sdk_apigatewayv2.types.integration_parameters
    import aws_sdk_apigatewayv2.types.selection_expression
    import aws_sdk_apigatewayv2.types.selection_key
    import aws_sdk_apigatewayv2.types.template_map


class CreateIntegrationResponseResponse(TypedDict, closed=True):
    content_handling_strategy: NotRequired[
        "aws_sdk_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
    ]
    """<p>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>"""
    integration_response_id: NotRequired["aws_sdk_apigatewayv2.types.id.Id"]
    """<p>The integration response ID.</p>"""
    integration_response_key: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
    ]
    """<p>The integration response key.</p>"""
    response_parameters: NotRequired[
        "aws_sdk_apigatewayv2.types.integration_parameters.IntegrationParameters"
    ]
    """<p>A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where name is a valid and unique response header name and JSON-expression is a valid JSON expression without the $ prefix.</p>"""
    response_templates: NotRequired[
        "aws_sdk_apigatewayv2.types.template_map.TemplateMap"
    ]
    """<p>The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.</p>"""
    template_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The template selection expressions for the integration response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationResponseResponse) -> dict:
    out: dict = {}
    if "content_handling_strategy" in value:
        import aws_sdk_apigatewayv2.types.content_handling_strategy

        out["contentHandlingStrategy"] = (
            aws_sdk_apigatewayv2.types.content_handling_strategy.serialize_json(
                value["content_handling_strategy"]
            )
        )
    if "integration_response_id" in value:
        out["integrationResponseId"] = value["integration_response_id"]
    if "integration_response_key" in value:
        out["integrationResponseKey"] = value["integration_response_key"]
    if "response_parameters" in value:
        import aws_sdk_apigatewayv2.types.integration_parameters

        out["responseParameters"] = (
            aws_sdk_apigatewayv2.types.integration_parameters.serialize_json(
                value["response_parameters"]
            )
        )
    if "response_templates" in value:
        import aws_sdk_apigatewayv2.types.template_map

        out["responseTemplates"] = (
            aws_sdk_apigatewayv2.types.template_map.serialize_json(
                value["response_templates"]
            )
        )
    if "template_selection_expression" in value:
        out["templateSelectionExpression"] = value["template_selection_expression"]
    return out


def deserialize_json(data: dict) -> CreateIntegrationResponseResponse:
    out: CreateIntegrationResponseResponse = {}  # type: ignore[typeddict-item]
    if "contentHandlingStrategy" in data:
        import aws_sdk_apigatewayv2.types.content_handling_strategy

        out["content_handling_strategy"] = (
            aws_sdk_apigatewayv2.types.content_handling_strategy.deserialize_json(
                data["contentHandlingStrategy"]
            )
        )
    if "integrationResponseId" in data:
        out["integration_response_id"] = data["integrationResponseId"]
    if "integrationResponseKey" in data:
        out["integration_response_key"] = data["integrationResponseKey"]
    if "responseParameters" in data:
        import aws_sdk_apigatewayv2.types.integration_parameters

        out["response_parameters"] = (
            aws_sdk_apigatewayv2.types.integration_parameters.deserialize_json(
                data["responseParameters"]
            )
        )
    if "responseTemplates" in data:
        import aws_sdk_apigatewayv2.types.template_map

        out["response_templates"] = (
            aws_sdk_apigatewayv2.types.template_map.deserialize_json(
                data["responseTemplates"]
            )
        )
    if "templateSelectionExpression" in data:
        out["template_selection_expression"] = data["templateSelectionExpression"]
    return out
