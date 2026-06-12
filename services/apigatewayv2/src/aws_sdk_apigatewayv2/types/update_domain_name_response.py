"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateDomainNameResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.arn
    import aws_sdk_apigatewayv2.types.domain_name_configurations
    import aws_sdk_apigatewayv2.types.mutual_tls_authentication
    import aws_sdk_apigatewayv2.types.routing_mode
    import aws_sdk_apigatewayv2.types.selection_expression
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and512
    import aws_sdk_apigatewayv2.types.tags


class UpdateDomainNameResponse(TypedDict):
    api_mapping_selection_expression: NotRequired[
        "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
    ]
    """<p>The API mapping selection expression.</p>"""
    domain_name: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and512.StringWithLengthBetween1And512"
    ]
    """<p>The name of the DomainName resource.</p>"""
    domain_name_arn: NotRequired["aws_sdk_apigatewayv2.types.arn.Arn"]
    """<p>The ARN of the DomainName resource.</p>"""
    domain_name_configurations: NotRequired[
        "aws_sdk_apigatewayv2.types.domain_name_configurations.DomainNameConfigurations"
    ]
    """<p>The domain name configurations.</p>"""
    mutual_tls_authentication: NotRequired[
        "aws_sdk_apigatewayv2.types.mutual_tls_authentication.MutualTlsAuthentication"
    ]
    """<p>The mutual TLS authentication configuration for a custom domain name.</p>"""
    routing_mode: NotRequired["aws_sdk_apigatewayv2.types.routing_mode.RoutingMode"]
    """<p>The routing mode.</p>"""
    tags: NotRequired["aws_sdk_apigatewayv2.types.tags.Tags"]
    """<p>The collection of tags associated with a domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainNameResponse) -> dict:
    out: dict = {}
    if "api_mapping_selection_expression" in value:
        out["apiMappingSelectionExpression"] = value["api_mapping_selection_expression"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "domain_name_arn" in value:
        out["domainNameArn"] = value["domain_name_arn"]
    if "domain_name_configurations" in value:
        import aws_sdk_apigatewayv2.types.domain_name_configurations

        out["domainNameConfigurations"] = (
            aws_sdk_apigatewayv2.types.domain_name_configurations.serialize_json(
                value["domain_name_configurations"]
            )
        )
    if "mutual_tls_authentication" in value:
        import aws_sdk_apigatewayv2.types.mutual_tls_authentication

        out["mutualTlsAuthentication"] = (
            aws_sdk_apigatewayv2.types.mutual_tls_authentication.serialize_json(
                value["mutual_tls_authentication"]
            )
        )
    if "routing_mode" in value:
        import aws_sdk_apigatewayv2.types.routing_mode

        out["routingMode"] = aws_sdk_apigatewayv2.types.routing_mode.serialize_json(
            value["routing_mode"]
        )
    if "tags" in value:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateDomainNameResponse:
    out: UpdateDomainNameResponse = {}  # type: ignore[typeddict-item]
    if "apiMappingSelectionExpression" in data:
        out["api_mapping_selection_expression"] = data["apiMappingSelectionExpression"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "domainNameArn" in data:
        out["domain_name_arn"] = data["domainNameArn"]
    if "domainNameConfigurations" in data:
        import aws_sdk_apigatewayv2.types.domain_name_configurations

        out["domain_name_configurations"] = (
            aws_sdk_apigatewayv2.types.domain_name_configurations.deserialize_json(
                data["domainNameConfigurations"]
            )
        )
    if "mutualTlsAuthentication" in data:
        import aws_sdk_apigatewayv2.types.mutual_tls_authentication

        out["mutual_tls_authentication"] = (
            aws_sdk_apigatewayv2.types.mutual_tls_authentication.deserialize_json(
                data["mutualTlsAuthentication"]
            )
        )
    if "routingMode" in data:
        import aws_sdk_apigatewayv2.types.routing_mode

        out["routing_mode"] = aws_sdk_apigatewayv2.types.routing_mode.deserialize_json(
            data["routingMode"]
        )
    if "tags" in data:
        import aws_sdk_apigatewayv2.types.tags

        out["tags"] = aws_sdk_apigatewayv2.types.tags.deserialize_json(data["tags"])
    return out
