"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetVpcOriginResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string
    import capo_cloudfront.types.vpc_origin


class GetVpcOriginResult(TypedDict, closed=True):
    vpc_origin: NotRequired["capo_cloudfront.types.vpc_origin.VpcOrigin"]
    """<p>The VPC origin.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The VPC origin ETag.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetVpcOriginResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "vpc_origin" in value:
        import capo_cloudfront.types.vpc_origin

        capo_cloudfront.types.vpc_origin.serialize_xml(
            value["vpc_origin"], el, "VpcOrigin"
        )


def deserialize_xml(el: Element) -> GetVpcOriginResult:
    out: GetVpcOriginResult = {}  # type: ignore[typeddict-item]
    child_vpc_origin = el.find("VpcOrigin")
    if child_vpc_origin is not None:
        import capo_cloudfront.types.vpc_origin

        out["vpc_origin"] = capo_cloudfront.types.vpc_origin.deserialize_xml(
            child_vpc_origin
        )
    return out
