"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayV2ApiDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cors_configuration
    import capo_securityhub.types.non_empty_string


class AwsApiGatewayV2ApiDetails(TypedDict, closed=True):
    api_endpoint: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The URI of the API. </p> <p>Uses the format <code> <i><api-id></i>.execute-api.<i><region></i>.amazonaws.com</code> </p> <p>The stage name is typically appended to the URI to form a complete path to a deployed API stage.</p>"""
    api_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the API.</p>"""
    api_key_selection_expression: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An API key selection expression. Supported only for WebSocket APIs. </p>"""
    created_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    r"""<p>Indicates when the API was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the API.</p>"""
    version: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The version identifier for the API.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the API.</p>"""
    protocol_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The API protocol for the API.</p> <p>Valid values: <code>WEBSOCKET</code> | <code>HTTP</code> </p>"""
    route_selection_expression: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The route selection expression for the API.</p> <p>For HTTP APIs, must be <code>${request.method} ${request.path}</code>. This is the default value for HTTP APIs.</p> <p>For WebSocket APIs, there is no default value.</p>"""
    cors_configuration: NotRequired[
        "capo_securityhub.types.aws_cors_configuration.AwsCorsConfiguration"
    ]
    """<p>A cross-origin resource sharing (CORS) configuration. Supported only for HTTP APIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayV2ApiDetails) -> dict:
    out: dict = {}
    if "api_endpoint" in value:
        out["ApiEndpoint"] = value["api_endpoint"]
    if "api_id" in value:
        out["ApiId"] = value["api_id"]
    if "api_key_selection_expression" in value:
        out["ApiKeySelectionExpression"] = value["api_key_selection_expression"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    if "description" in value:
        out["Description"] = value["description"]
    if "version" in value:
        out["Version"] = value["version"]
    if "name" in value:
        out["Name"] = value["name"]
    if "protocol_type" in value:
        out["ProtocolType"] = value["protocol_type"]
    if "route_selection_expression" in value:
        out["RouteSelectionExpression"] = value["route_selection_expression"]
    if "cors_configuration" in value:
        import capo_securityhub.types.aws_cors_configuration

        out["CorsConfiguration"] = (
            capo_securityhub.types.aws_cors_configuration.serialize_json(
                value["cors_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsApiGatewayV2ApiDetails:
    out: AwsApiGatewayV2ApiDetails = {}  # type: ignore[typeddict-item]
    if "ApiEndpoint" in data:
        out["api_endpoint"] = data["ApiEndpoint"]
    if "ApiId" in data:
        out["api_id"] = data["ApiId"]
    if "ApiKeySelectionExpression" in data:
        out["api_key_selection_expression"] = data["ApiKeySelectionExpression"]
    if "CreatedDate" in data:
        out["created_date"] = data["CreatedDate"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ProtocolType" in data:
        out["protocol_type"] = data["ProtocolType"]
    if "RouteSelectionExpression" in data:
        out["route_selection_expression"] = data["RouteSelectionExpression"]
    if "CorsConfiguration" in data:
        import capo_securityhub.types.aws_cors_configuration

        out["cors_configuration"] = (
            capo_securityhub.types.aws_cors_configuration.deserialize_json(
                data["CorsConfiguration"]
            )
        )
    return out
