"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateOriginAccessControlResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_access_control
    import aws_sdk_cloudfront.types.string


class CreateOriginAccessControlResult(TypedDict, closed=True):
    origin_access_control: NotRequired[
        "aws_sdk_cloudfront.types.origin_access_control.OriginAccessControl"
    ]
    """<p>Contains an origin access control.</p>"""
    location: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The URL of the origin access control.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the origin access control.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateOriginAccessControlResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "origin_access_control" in value:
        import aws_sdk_cloudfront.types.origin_access_control

        aws_sdk_cloudfront.types.origin_access_control.serialize_xml(
            value["origin_access_control"], el, "OriginAccessControl"
        )


def deserialize_xml(el: Element) -> CreateOriginAccessControlResult:
    out: CreateOriginAccessControlResult = {}  # type: ignore[typeddict-item]
    child_origin_access_control = el.find("OriginAccessControl")
    if child_origin_access_control is not None:
        import aws_sdk_cloudfront.types.origin_access_control

        out["origin_access_control"] = (
            aws_sdk_cloudfront.types.origin_access_control.deserialize_xml(
                child_origin_access_control
            )
        )
    return out
