"""Generated from Smithy shape ``com.amazonaws.cloudfront#Restrictions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.geo_restriction


class Restrictions(TypedDict, closed=True):
    geo_restriction: "capo_cloudfront.types.geo_restriction.GeoRestriction"
    """<p>A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using <code>MaxMind</code> GeoIP databases.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Restrictions, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.geo_restriction

    capo_cloudfront.types.geo_restriction.serialize_xml(
        value["geo_restriction"], el, "GeoRestriction"
    )


def deserialize_xml(el: Element) -> Restrictions:
    out: Restrictions = {}  # type: ignore[typeddict-item]
    child_geo_restriction = el.find("GeoRestriction")
    if child_geo_restriction is not None:
        import capo_cloudfront.types.geo_restriction

        out["geo_restriction"] = capo_cloudfront.types.geo_restriction.deserialize_xml(
            child_geo_restriction
        )
    else:
        raise DeserializationError("Restrictions.geo_restriction required")
    return out
