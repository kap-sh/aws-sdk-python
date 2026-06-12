"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateApiResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.__list_of__string
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.__timestamp_iso8601
    import aws_sdk_apigatewayv2.types.cors
    import aws_sdk_apigatewayv2.types.id
    import aws_sdk_apigatewayv2.types.ip_address_type
    import aws_sdk_apigatewayv2.types.protocol_type
    import aws_sdk_apigatewayv2.types.selection_expression
    import aws_sdk_apigatewayv2.types.string_with_length_between0_and1024
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and128
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and64
    import aws_sdk_apigatewayv2.types.tags


class CreateApiResponse(TypedDict):
    api_endpoint: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.</p>"""
    api_gateway_managed: NotRequired["aws_sdk_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether an API is managed by API Gateway. You can't update or delete a managed API by using API Gateway. A managed API can be deleted only through the tooling or service that created it.</p>"""
    api_id: NotRequired["aws_sdk_apigatewayv2.types.id.Id"]
    """<p>The API ID.</p>"""
    api_key_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>An API key selection expression. Supported only for WebSocket APIs. See <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\">API Key Selection Expressions</a>.</p>"""
    cors_configuration: NotRequired["aws_sdk_apigatewayv2.types.cors.Cors"]
    """<p>A CORS configuration. Supported only for HTTP APIs.</p>"""
    created_date: NotRequired[
        "aws_sdk_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the API was created.</p>"""
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
    import_info: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of__string.__listOf__string"
    ]
    """<p>The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.</p>"""
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
    route_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</p>"""
    tags: NotRequired["aws_sdk_apigatewayv2.types.tags.Tags"]
    """<p>A collection of tags associated with the API.</p>"""
    version: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    ]
    """<p>A version identifier for the API.</p>"""
    warnings: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of__string.__listOf__string"
    ]
    """<p>The warning messages reported when failonwarnings is turned on during API import.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiResponse) -> dict:
    out: dict = {}
    if "api_endpoint" in value:
        out["apiEndpoint"] = value["api_endpoint"]
    if "api_gateway_managed" in value:
        out["apiGatewayManaged"] = value["api_gateway_managed"]
    if "api_id" in value:
        out["apiId"] = value["api_id"]
    if "api_key_selection_expression" in value:
        out["apiKeySelectionExpression"] = value["api_key_selection_expression"]
    if "cors_configuration" in value:
        import aws_sdk_apigatewayv2.types.cors

        out["corsConfiguration"] = aws_sdk_apigatewayv2.types.cors.serialize_json(
            value["cors_configuration"]
        )
    if "created_date" in value:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["createdDate"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["created_date"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "disable_schema_validation" in value:
        out["disableSchemaValidation"] = value["disable_schema_validation"]
    if "disable_execute_api_endpoint" in value:
        out["disableExecuteApiEndpoint"] = value["disable_execute_api_endpoint"]
    if "import_info" in value:
        import aws_sdk_apigatewayv2.types.__list_of__string

        out["importInfo"] = aws_sdk_apigatewayv2.types.__list_of__string.serialize_json(
            value["import_info"]
        )
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
    if "route_selection_expression" in value:
        out["routeSelectionExpression"] = value["route_selection_expression"]
    if "tags" in value:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.serialize_json(value["tags"])
    if "version" in value:
        out["version"] = value["version"]
    if "warnings" in value:
        import aws_sdk_apigatewayv2.types.__list_of__string

        out["warnings"] = aws_sdk_apigatewayv2.types.__list_of__string.serialize_json(
            value["warnings"]
        )
    return out


def deserialize_json(data: dict) -> CreateApiResponse:
    out: CreateApiResponse = {}  # type: ignore[typeddict-item]
    if "apiEndpoint" in data:
        out["api_endpoint"] = data["apiEndpoint"]
    if "apiGatewayManaged" in data:
        out["api_gateway_managed"] = data["apiGatewayManaged"]
    if "apiId" in data:
        out["api_id"] = data["apiId"]
    if "apiKeySelectionExpression" in data:
        out["api_key_selection_expression"] = data["apiKeySelectionExpression"]
    if "corsConfiguration" in data:
        import aws_sdk_apigatewayv2.types.cors

        out["cors_configuration"] = aws_sdk_apigatewayv2.types.cors.deserialize_json(
            data["corsConfiguration"]
        )
    if "createdDate" in data:
        import aws_sdk_apigatewayv2.types.__timestamp_iso8601

        out["created_date"] = (
            aws_sdk_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["createdDate"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "disableSchemaValidation" in data:
        out["disable_schema_validation"] = data["disableSchemaValidation"]
    if "disableExecuteApiEndpoint" in data:
        out["disable_execute_api_endpoint"] = data["disableExecuteApiEndpoint"]
    if "importInfo" in data:
        import aws_sdk_apigatewayv2.types.__list_of__string

        out["import_info"] = (
            aws_sdk_apigatewayv2.types.__list_of__string.deserialize_json(
                data["importInfo"]
            )
        )
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
    if "routeSelectionExpression" in data:
        out["route_selection_expression"] = data["routeSelectionExpression"]
    if "tags" in data:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.deserialize_json(data["tags"])
    if "version" in data:
        out["version"] = data["version"]
    if "warnings" in data:
        import aws_sdk_apigatewayv2.types.__list_of__string

        out["warnings"] = aws_sdk_apigatewayv2.types.__list_of__string.deserialize_json(
            data["warnings"]
        )
    return out
