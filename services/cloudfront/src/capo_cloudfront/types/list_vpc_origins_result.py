"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListVpcOriginsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.vpc_origin_list


class ListVpcOriginsResult(TypedDict, closed=True):
    vpc_origin_list: NotRequired["capo_cloudfront.types.vpc_origin_list.VpcOriginList"]
    """<p>List of VPC origins.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListVpcOriginsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "vpc_origin_list" in value:
        import capo_cloudfront.types.vpc_origin_list

        capo_cloudfront.types.vpc_origin_list.serialize_xml(
            value["vpc_origin_list"], el, "VpcOriginList"
        )


def deserialize_xml(el: Element) -> ListVpcOriginsResult:
    out: ListVpcOriginsResult = {}  # type: ignore[typeddict-item]
    child_vpc_origin_list = el.find("VpcOriginList")
    if child_vpc_origin_list is not None:
        import capo_cloudfront.types.vpc_origin_list

        out["vpc_origin_list"] = capo_cloudfront.types.vpc_origin_list.deserialize_xml(
            child_vpc_origin_list
        )
    return out
