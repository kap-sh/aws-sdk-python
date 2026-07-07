"""Generated from Smithy shape ``com.amazonaws.s3#Delete``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.object_identifier_list
    import aws_sdk_s3.types.quiet


class Delete(TypedDict, closed=True):
    objects: "aws_sdk_s3.types.object_identifier_list.ObjectIdentifierList"
    """<p>The object to delete.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, an object that's composed entirely of whitespace characters is not supported by the <code>DeleteObjects</code> API operation. The request will receive a <code>400 Bad Request</code> error and none of the objects in the request will be deleted.</p> </note>"""
    quiet: NotRequired["aws_sdk_s3.types.quiet.Quiet"]
    """<p>Element to enable quiet mode for the request. When you add this element, you must set its value to <code>true</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Delete, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.object_identifier_list

    aws_sdk_s3.types.object_identifier_list.serialize_xml_flat(
        value["objects"], el, "Object"
    )
    if "quiet" in value:
        SubElement(el, "Quiet").text = "true" if value["quiet"] else "false"


def deserialize_xml(el: Element) -> Delete:
    out: Delete = {}  # type: ignore[typeddict-item]
    if el.find("Object") is not None:
        import aws_sdk_s3.types.object_identifier_list

        out["objects"] = aws_sdk_s3.types.object_identifier_list.deserialize_xml_flat(
            el, "Object"
        )
    else:
        raise DeserializationError("Delete.objects required")
    child_quiet = el.find("Quiet")
    if child_quiet is not None:
        out["quiet"] = (child_quiet.text or "").lower() == "true"
    return out
