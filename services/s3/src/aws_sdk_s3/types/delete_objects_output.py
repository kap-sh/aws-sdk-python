"""Generated from Smithy shape ``com.amazonaws.s3#DeleteObjectsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.deleted_objects
    import aws_sdk_s3.types.errors
    import aws_sdk_s3.types.request_charged


class DeleteObjectsOutput(TypedDict, closed=True):
    deleted: NotRequired["aws_sdk_s3.types.deleted_objects.DeletedObjects"]
    """<p>Container element for a successful delete. It identifies the object that was successfully deleted.</p>"""
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]
    errors: NotRequired["aws_sdk_s3.types.errors.Errors"]
    """<p>Container for a failed delete action that describes the object that Amazon S3 attempted to delete and the error it encountered.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteObjectsOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "deleted" in value:
        import aws_sdk_s3.types.deleted_objects

        aws_sdk_s3.types.deleted_objects.serialize_xml_flat(
            value["deleted"], el, "Deleted"
        )
    if "errors" in value:
        import aws_sdk_s3.types.errors

        aws_sdk_s3.types.errors.serialize_xml_flat(value["errors"], el, "Error")


def deserialize_xml(el: Element) -> DeleteObjectsOutput:
    out: DeleteObjectsOutput = {}  # type: ignore[typeddict-item]
    if el.find("Deleted") is not None:
        import aws_sdk_s3.types.deleted_objects

        out["deleted"] = aws_sdk_s3.types.deleted_objects.deserialize_xml_flat(
            el, "Deleted"
        )
    if el.find("Error") is not None:
        import aws_sdk_s3.types.errors

        out["errors"] = aws_sdk_s3.types.errors.deserialize_xml_flat(el, "Error")
    return out
