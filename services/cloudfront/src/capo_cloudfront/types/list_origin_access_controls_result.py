"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListOriginAccessControlsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_access_control_list


class ListOriginAccessControlsResult(TypedDict, closed=True):
    origin_access_control_list: NotRequired[
        "capo_cloudfront.types.origin_access_control_list.OriginAccessControlList"
    ]
    """<p>A list of origin access controls.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListOriginAccessControlsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "origin_access_control_list" in value:
        import capo_cloudfront.types.origin_access_control_list

        capo_cloudfront.types.origin_access_control_list.serialize_xml(
            value["origin_access_control_list"], el, "OriginAccessControlList"
        )


def deserialize_xml(el: Element) -> ListOriginAccessControlsResult:
    out: ListOriginAccessControlsResult = {}  # type: ignore[typeddict-item]
    child_origin_access_control_list = el.find("OriginAccessControlList")
    if child_origin_access_control_list is not None:
        import capo_cloudfront.types.origin_access_control_list

        out["origin_access_control_list"] = (
            capo_cloudfront.types.origin_access_control_list.deserialize_xml(
                child_origin_access_control_list
            )
        )
    return out
