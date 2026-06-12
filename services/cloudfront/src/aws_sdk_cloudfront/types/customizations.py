"""Generated from Smithy shape ``com.amazonaws.cloudfront#Customizations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.certificate
    import aws_sdk_cloudfront.types.geo_restriction_customization
    import aws_sdk_cloudfront.types.web_acl_customization


class Customizations(TypedDict):
    web_acl: NotRequired[
        "aws_sdk_cloudfront.types.web_acl_customization.WebAclCustomization"
    ]
    """<p>The WAF web ACL.</p>"""
    certificate: NotRequired["aws_sdk_cloudfront.types.certificate.Certificate"]
    """<p>The Certificate Manager (ACM) certificate.</p>"""
    geo_restrictions: NotRequired[
        "aws_sdk_cloudfront.types.geo_restriction_customization.GeoRestrictionCustomization"
    ]
    """<p>The geographic restrictions.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Customizations, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "web_acl" in value:
        import aws_sdk_cloudfront.types.web_acl_customization

        aws_sdk_cloudfront.types.web_acl_customization.serialize_xml(
            value["web_acl"], el, "WebAcl"
        )
    if "certificate" in value:
        import aws_sdk_cloudfront.types.certificate

        aws_sdk_cloudfront.types.certificate.serialize_xml(
            value["certificate"], el, "Certificate"
        )
    if "geo_restrictions" in value:
        import aws_sdk_cloudfront.types.geo_restriction_customization

        aws_sdk_cloudfront.types.geo_restriction_customization.serialize_xml(
            value["geo_restrictions"], el, "GeoRestrictions"
        )


def deserialize_xml(el: Element) -> Customizations:
    out: Customizations = {}  # type: ignore[typeddict-item]
    child_web_acl = el.find("WebAcl")
    if child_web_acl is not None:
        import aws_sdk_cloudfront.types.web_acl_customization

        out["web_acl"] = aws_sdk_cloudfront.types.web_acl_customization.deserialize_xml(
            child_web_acl
        )
    child_certificate = el.find("Certificate")
    if child_certificate is not None:
        import aws_sdk_cloudfront.types.certificate

        out["certificate"] = aws_sdk_cloudfront.types.certificate.deserialize_xml(
            child_certificate
        )
    child_geo_restrictions = el.find("GeoRestrictions")
    if child_geo_restrictions is not None:
        import aws_sdk_cloudfront.types.geo_restriction_customization

        out["geo_restrictions"] = (
            aws_sdk_cloudfront.types.geo_restriction_customization.deserialize_xml(
                child_geo_restrictions
            )
        )
    return out
