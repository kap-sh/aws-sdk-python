"""Generated from Smithy shape ``com.amazonaws.s3#Initiator``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.display_name
    import aws_sdk_s3.types.id


class Initiator(TypedDict):
    id: NotRequired["aws_sdk_s3.types.id.ID"]
    """<p>If the principal is an Amazon Web Services account, it provides the Canonical User ID. If the principal is an IAM User, it provides a user ARN value.</p> <note> <p> <b>Directory buckets</b> - If the principal is an Amazon Web Services account, it provides the Amazon Web Services account ID. If the principal is an IAM User, it provides a user ARN value.</p> </note>"""
    display_name: NotRequired["aws_sdk_s3.types.display_name.DisplayName"]
    """<p></p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: Initiator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "ID").text = str(value["id"])
    if "display_name" in value:
        SubElement(el, "DisplayName").text = str(value["display_name"])


def deserialize_xml(el: Element) -> Initiator:
    out: Initiator = {}  # type: ignore[typeddict-item]
    child_id = el.find("ID")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_display_name = el.find("DisplayName")
    if child_display_name is not None:
        out["display_name"] = str(child_display_name.text or "")
    return out
