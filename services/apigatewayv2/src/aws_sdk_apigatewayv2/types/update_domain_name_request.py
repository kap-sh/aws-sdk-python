"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#UpdateDomainNameRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.domain_name_configurations
    import aws_sdk_apigatewayv2.types.mutual_tls_authentication_input
    import aws_sdk_apigatewayv2.types.routing_mode


class UpdateDomainNameRequest(TypedDict):
    domain_name: "aws_sdk_apigatewayv2.types.__string.__string"
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


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainNameRequest) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> UpdateDomainNameRequest:
    out: UpdateDomainNameRequest = {}  # type: ignore[typeddict-item]
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
    return out
