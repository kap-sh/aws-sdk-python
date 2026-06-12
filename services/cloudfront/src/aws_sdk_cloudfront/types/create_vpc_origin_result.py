"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateVpcOriginResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.vpc_origin


class CreateVpcOriginResult(TypedDict):
    vpc_origin: NotRequired["aws_sdk_cloudfront.types.vpc_origin.VpcOrigin"]
    """<p>The VPC origin.</p>"""
    location: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The VPC origin location.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The VPC origin ETag.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateVpcOriginResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "vpc_origin" in value:
        import aws_sdk_cloudfront.types.vpc_origin

        aws_sdk_cloudfront.types.vpc_origin.serialize_xml(
            value["vpc_origin"], el, "VpcOrigin"
        )


def deserialize_xml(el: Element) -> CreateVpcOriginResult:
    out: CreateVpcOriginResult = {}  # type: ignore[typeddict-item]
    child_vpc_origin = el.find("VpcOrigin")
    if child_vpc_origin is not None:
        import aws_sdk_cloudfront.types.vpc_origin

        out["vpc_origin"] = aws_sdk_cloudfront.types.vpc_origin.deserialize_xml(
            child_vpc_origin
        )
    return out
