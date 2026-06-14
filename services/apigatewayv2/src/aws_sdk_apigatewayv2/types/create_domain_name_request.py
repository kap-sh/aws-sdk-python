"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CreateDomainNameRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.domain_name_configurations
    import aws_sdk_apigatewayv2.types.mutual_tls_authentication_input
    import aws_sdk_apigatewayv2.types.routing_mode
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and512
    import aws_sdk_apigatewayv2.types.tags


class CreateDomainNameRequest(TypedDict):
    domain_name: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and512.StringWithLengthBetween1And512"
    ]
    """<p>The domain name.</p>"""
    domain_name_configurations: NotRequired[
        "aws_sdk_apigatewayv2.types.domain_name_configurations.DomainNameConfigurations"
    ]
    """<p>The domain name configurations.</p>"""
    mutual_tls_authentication: NotRequired[
        "aws_sdk_apigatewayv2.types.mutual_tls_authentication_input.MutualTlsAuthenticationInput"
    ]
    """<p>The mutual TLS authentication configuration for a custom domain name.</p>"""
    routing_mode: NotRequired["aws_sdk_apigatewayv2.types.routing_mode.RoutingMode"]
    """<p>The routing mode.</p>"""
    tags: NotRequired["aws_sdk_apigatewayv2.types.tags.Tags"]
    """<p>The collection of tags associated with a domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainNameRequest) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "domain_name_configurations" in value:
        import aws_sdk_apigatewayv2.types.domain_name_configurations

        out["domainNameConfigurations"] = (
            aws_sdk_apigatewayv2.types.domain_name_configurations.serialize_json(
                value["domain_name_configurations"]
            )
        )
    if "mutual_tls_authentication" in value:
        import aws_sdk_apigatewayv2.types.mutual_tls_authentication_input

        out["mutualTlsAuthentication"] = (
            aws_sdk_apigatewayv2.types.mutual_tls_authentication_input.serialize_json(
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


def deserialize_json(data: dict) -> CreateDomainNameRequest:
    out: CreateDomainNameRequest = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "domainNameConfigurations" in data:
        import aws_sdk_apigatewayv2.types.domain_name_configurations

        out["domain_name_configurations"] = (
            aws_sdk_apigatewayv2.types.domain_name_configurations.deserialize_json(
                data["domainNameConfigurations"]
            )
        )
    if "mutualTlsAuthentication" in data:
        import aws_sdk_apigatewayv2.types.mutual_tls_authentication_input

        out["mutual_tls_authentication"] = (
            aws_sdk_apigatewayv2.types.mutual_tls_authentication_input.deserialize_json(
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
