"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateOriginAccessControlResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_access_control
    import capo_cloudfront.types.string


class UpdateOriginAccessControlResult(TypedDict, closed=True):
    origin_access_control: NotRequired[
        "capo_cloudfront.types.origin_access_control.OriginAccessControl"
    ]
    """<p>The origin access control after it has been updated.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The new version of the origin access control after it has been updated.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateOriginAccessControlResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "origin_access_control" in value:
        import capo_cloudfront.types.origin_access_control

        capo_cloudfront.types.origin_access_control.serialize_xml(
            value["origin_access_control"], el, "OriginAccessControl"
        )


def deserialize_xml(el: Element) -> UpdateOriginAccessControlResult:
    out: UpdateOriginAccessControlResult = {}  # type: ignore[typeddict-item]
    child_origin_access_control = el.find("OriginAccessControl")
    if child_origin_access_control is not None:
        import capo_cloudfront.types.origin_access_control

        out["origin_access_control"] = (
            capo_cloudfront.types.origin_access_control.deserialize_xml(
                child_origin_access_control
            )
        )
    return out
