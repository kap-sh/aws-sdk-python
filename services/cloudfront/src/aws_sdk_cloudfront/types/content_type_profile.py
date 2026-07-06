"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContentTypeProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.format
    import aws_sdk_cloudfront.types.string


class ContentTypeProfile(TypedDict, closed=True):
    format: "aws_sdk_cloudfront.types.format.Format"
    """<p>The format for a field-level encryption content type-profile mapping.</p>"""
    profile_id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The profile ID for a field-level encryption content type-profile mapping.</p>"""
    content_type: "aws_sdk_cloudfront.types.string.string"
    """<p>The content type for a field-level encryption content type-profile mapping.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ContentTypeProfile, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.format

    aws_sdk_cloudfront.types.format.serialize_xml(value["format"], el, "Format")
    if "profile_id" in value:
        SubElement(el, "ProfileId").text = str(value["profile_id"])
    SubElement(el, "ContentType").text = str(value["content_type"])


def deserialize_xml(el: Element) -> ContentTypeProfile:
    out: ContentTypeProfile = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import aws_sdk_cloudfront.types.format

        out["format"] = aws_sdk_cloudfront.types.format.deserialize_xml(child_format)
    else:
        raise DeserializationError("ContentTypeProfile.format required")
    child_profile_id = el.find("ProfileId")
    if child_profile_id is not None:
        out["profile_id"] = str(child_profile_id.text or "")
    child_content_type = el.find("ContentType")
    if child_content_type is not None:
        out["content_type"] = str(child_content_type.text or "")
    else:
        raise DeserializationError("ContentTypeProfile.content_type required")
    return out
