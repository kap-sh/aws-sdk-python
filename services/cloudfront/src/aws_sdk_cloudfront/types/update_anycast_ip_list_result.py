"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateAnycastIpListResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.anycast_ip_list
    import aws_sdk_cloudfront.types.string


class UpdateAnycastIpListResult(TypedDict, closed=True):
    anycast_ip_list: NotRequired[
        "aws_sdk_cloudfront.types.anycast_ip_list.AnycastIpList"
    ]
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the Anycast static IP list.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateAnycastIpListResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "anycast_ip_list" in value:
        import aws_sdk_cloudfront.types.anycast_ip_list

        aws_sdk_cloudfront.types.anycast_ip_list.serialize_xml(
            value["anycast_ip_list"], el, "AnycastIpList"
        )


def deserialize_xml(el: Element) -> UpdateAnycastIpListResult:
    out: UpdateAnycastIpListResult = {}  # type: ignore[typeddict-item]
    child_anycast_ip_list = el.find("AnycastIpList")
    if child_anycast_ip_list is not None:
        import aws_sdk_cloudfront.types.anycast_ip_list

        out["anycast_ip_list"] = (
            aws_sdk_cloudfront.types.anycast_ip_list.deserialize_xml(
                child_anycast_ip_list
            )
        )
    return out
