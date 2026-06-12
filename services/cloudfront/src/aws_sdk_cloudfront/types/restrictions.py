"""Generated from Smithy shape ``com.amazonaws.cloudfront#Restrictions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.geo_restriction


class Restrictions(TypedDict):
    geo_restriction: "aws_sdk_cloudfront.types.geo_restriction.GeoRestriction"
    """<p>A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using <code>MaxMind</code> GeoIP databases.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Restrictions, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.geo_restriction

    aws_sdk_cloudfront.types.geo_restriction.serialize_xml(
        value["geo_restriction"], el, "GeoRestriction"
    )


def deserialize_xml(el: Element) -> Restrictions:
    out: Restrictions = {}  # type: ignore[typeddict-item]
    child_geo_restriction = el.find("GeoRestriction")
    if child_geo_restriction is not None:
        import aws_sdk_cloudfront.types.geo_restriction

        out["geo_restriction"] = (
            aws_sdk_cloudfront.types.geo_restriction.deserialize_xml(
                child_geo_restriction
            )
        )
    else:
        raise DeserializationError("Restrictions.geo_restriction required")
    return out
