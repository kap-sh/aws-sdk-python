"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectOwner``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.non_empty_max_length1024_string


class S3ObjectOwner(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""
    display_name: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3ObjectOwner, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "ID").text = str(value["id"])
    if "display_name" in value:
        SubElement(el, "DisplayName").text = str(value["display_name"])


def deserialize_xml(el: Element) -> S3ObjectOwner:
    out: S3ObjectOwner = {}  # type: ignore[typeddict-item]
    child_id = el.find("ID")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_display_name = el.find("DisplayName")
    if child_display_name is not None:
        out["display_name"] = str(child_display_name.text or "")
    return out
