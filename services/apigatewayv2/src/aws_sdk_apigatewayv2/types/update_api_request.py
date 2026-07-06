"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.arn
    import aws_sdk_apigatewayv2.types.cors
    import aws_sdk_apigatewayv2.types.ip_address_type
    import aws_sdk_apigatewayv2.types.selection_expression
    import aws_sdk_apigatewayv2.types.selection_key
    import aws_sdk_apigatewayv2.types.string_with_length_between0_and1024
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and64
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and128
    import aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048


class UpdateApiRequest(TypedDict, closed=True):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    api_key_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    r"""<p>An API key selection expression. Supported only for WebSocket APIs. See <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\">API Key Selection Expressions</a>.</p>"""
    cors_configuration: NotRequired["aws_sdk_apigatewayv2.types.cors.Cors"]
    """<p>A CORS configuration. Supported only for HTTP APIs.</p>"""
    credentials_arn: NotRequired["aws_sdk_apigatewayv2.types.arn.Arn"]
    """<p>This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, don't specify this parameter. Currently, this property is not used for HTTP integrations. If provided, this value replaces the credentials associated with the quick create integration. Supported only for HTTP APIs.</p>"""
    description: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
    ]
    """<p>The description of the API.</p>"""
    disable_schema_validation: NotRequired[
        "aws_sdk_apigatewayv2.types.__boolean.__boolean"
    ]
    """<p>Avoid validating models when creating a deployment. Supported only for WebSocket APIs.</p>"""
    disable_execute_api_endpoint: NotRequired[
        "aws_sdk_apigatewayv2.types.__boolean.__boolean"
    ]
    """<p>Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_apigatewayv2.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address types that can invoke your API or domain name.</p>"""
    name: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The name of the API.</p>"""
    route_key: NotRequired["aws_sdk_apigatewayv2.types.selection_key.SelectionKey"]
    """<p>This property is part of quick create. If not specified, the route created using quick create is kept. Otherwise, this value replaces the route key of the quick create route. Additional routes may still be added after the API is updated. Supported only for HTTP APIs.</p>"""
    route_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</p>"""
    target: NotRequired[
        "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
    ]
    """<p>This property is part of quick create. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. The value provided updates the integration URI and integration type. You can update a quick-created target, but you can't remove it from an API. Supported only for HTTP APIs.</p>"""
    version: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    ]
    """<p>A version identifier for the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApiRequest) -> dict:
    out: dict = {}
    if "api_key_selection_expression" in value:
        out["apiKeySelectionExpression"] = value["api_key_selection_expression"]
    if "cors_configuration" in value:
        import aws_sdk_apigatewayv2.types.cors

        out["corsConfiguration"] = aws_sdk_apigatewayv2.types.cors.serialize_json(
            value["cors_configuration"]
        )
    if "credentials_arn" in value:
        out["credentialsArn"] = value["credentials_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "disable_schema_validation" in value:
        out["disableSchemaValidation"] = value["disable_schema_validation"]
    if "disable_execute_api_endpoint" in value:
        out["disableExecuteApiEndpoint"] = value["disable_execute_api_endpoint"]
    if "ip_address_type" in value:
        import aws_sdk_apigatewayv2.types.ip_address_type

        out["ipAddressType"] = (
            aws_sdk_apigatewayv2.types.ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "route_key" in value:
        out["routeKey"] = value["route_key"]
    if "route_selection_expression" in value:
        out["routeSelectionExpression"] = value["route_selection_expression"]
    if "target" in value:
        out["target"] = value["target"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> UpdateApiRequest:
    out: UpdateApiRequest = {}  # type: ignore[typeddict-item]
    if "apiKeySelectionExpression" in data:
        out["api_key_selection_expression"] = data["apiKeySelectionExpression"]
    if "corsConfiguration" in data:
        import aws_sdk_apigatewayv2.types.cors

        out["cors_configuration"] = aws_sdk_apigatewayv2.types.cors.deserialize_json(
            data["corsConfiguration"]
        )
    if "credentialsArn" in data:
        out["credentials_arn"] = data["credentialsArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "disableSchemaValidation" in data:
        out["disable_schema_validation"] = data["disableSchemaValidation"]
    if "disableExecuteApiEndpoint" in data:
        out["disable_execute_api_endpoint"] = data["disableExecuteApiEndpoint"]
    if "ipAddressType" in data:
        import aws_sdk_apigatewayv2.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_apigatewayv2.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "routeKey" in data:
        out["route_key"] = data["routeKey"]
    if "routeSelectionExpression" in data:
        out["route_selection_expression"] = data["routeSelectionExpression"]
    if "target" in data:
        out["target"] = data["target"]
    if "version" in data:
        out["version"] = data["version"]
    return out
