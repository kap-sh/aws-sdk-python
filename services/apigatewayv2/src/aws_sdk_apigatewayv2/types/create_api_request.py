"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateApiRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.arn
    import aws_sdk_apigatewayv2.types.cors
    import aws_sdk_apigatewayv2.types.ip_address_type
    import aws_sdk_apigatewayv2.types.protocol_type
    import aws_sdk_apigatewayv2.types.selection_expression
    import aws_sdk_apigatewayv2.types.selection_key
    import aws_sdk_apigatewayv2.types.string_with_length_between0_and1024
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and64
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and128
    import aws_sdk_apigatewayv2.types.tags
    import aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048


class CreateApiRequest(TypedDict):
    api_key_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    r"""<p>An API key selection expression. Supported only for WebSocket APIs. See <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\">API Key Selection Expressions</a>.</p>"""
    cors_configuration: NotRequired["aws_sdk_apigatewayv2.types.cors.Cors"]
    r"""<p>A CORS configuration. Supported only for HTTP APIs. See <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html\">Configuring CORS</a> for more information.</p>"""
    credentials_arn: NotRequired["aws_sdk_apigatewayv2.types.arn.Arn"]
    """<p>This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null. Currently, this property is not used for HTTP integrations. Supported only for HTTP APIs.</p>"""
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
    """<p>The IP address types that can invoke the API.</p>"""
    name: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The name of the API.</p>"""
    protocol_type: NotRequired["aws_sdk_apigatewayv2.types.protocol_type.ProtocolType"]
    """<p>The API protocol.</p>"""
    route_key: NotRequired["aws_sdk_apigatewayv2.types.selection_key.SelectionKey"]
    """<p>This property is part of quick create. If you don't specify a routeKey, a default route of $default is created. The $default route acts as a catch-all for any request made to your API, for a particular stage. The $default route key can't be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.</p>"""
    route_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</p>"""
    tags: NotRequired["aws_sdk_apigatewayv2.types.tags.Tags"]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""
    target: NotRequired[
        "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
    ]
    """<p>This property is part of quick create. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.</p>"""
    version: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    ]
    """<p>A version identifier for the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiRequest) -> dict:
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
    if "protocol_type" in value:
        import aws_sdk_apigatewayv2.types.protocol_type

        out["protocolType"] = aws_sdk_apigatewayv2.types.protocol_type.serialize_json(
            value["protocol_type"]
        )
    if "route_key" in value:
        out["routeKey"] = value["route_key"]
    if "route_selection_expression" in value:
        out["routeSelectionExpression"] = value["route_selection_expression"]
    if "tags" in value:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.serialize_json(value["tags"])
    if "target" in value:
        out["target"] = value["target"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> CreateApiRequest:
    out: CreateApiRequest = {}  # type: ignore[typeddict-item]
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
    if "protocolType" in data:
        import aws_sdk_apigatewayv2.types.protocol_type

        out["protocol_type"] = (
            aws_sdk_apigatewayv2.types.protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    if "routeKey" in data:
        out["route_key"] = data["routeKey"]
    if "routeSelectionExpression" in data:
        out["route_selection_expression"] = data["routeSelectionExpression"]
    if "tags" in data:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.deserialize_json(data["tags"])
    if "target" in data:
        out["target"] = data["target"]
    if "version" in data:
        out["version"] = data["version"]
    return out
