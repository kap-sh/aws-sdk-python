"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#EndpointConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min1_max64
    import aws_sdk_apigatewayv2.types.__string_min3_max256
    import aws_sdk_apigatewayv2.types.__string_min10_max2048


class EndpointConfigurationResponse(TypedDict, closed=True):
    certificate_arn: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min10_max2048.__stringMin10Max2048"
    ]
    """<p>The ARN of the ACM certificate.</p>"""
    domain_name: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min3_max256.__stringMin3Max256"
    ]
    """<p>The domain name.</p>"""
    portal_default_domain_name: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min3_max256.__stringMin3Max256"
    ]
    """<p>The portal default domain name. This domain name is generated and managed by API Gateway.</p>"""
    portal_domain_hosted_zone_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max64.__stringMin1Max64"
    ]
    """<p>The portal domain hosted zone identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointConfigurationResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "portal_default_domain_name" in value:
        out["portalDefaultDomainName"] = value["portal_default_domain_name"]
    if "portal_domain_hosted_zone_id" in value:
        out["portalDomainHostedZoneId"] = value["portal_domain_hosted_zone_id"]
    return out


def deserialize_json(data: dict) -> EndpointConfigurationResponse:
    out: EndpointConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "portalDefaultDomainName" in data:
        out["portal_default_domain_name"] = data["portalDefaultDomainName"]
    if "portalDomainHostedZoneId" in data:
        out["portal_domain_hosted_zone_id"] = data["portalDomainHostedZoneId"]
    return out
