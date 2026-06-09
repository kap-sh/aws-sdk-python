"""Generated from Smithy shape ``com.amazonaws.s3#DeleteMarkerReplication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.delete_marker_replication_status


class DeleteMarkerReplication(TypedDict):
    status: NotRequired[
        "aws_sdk_s3.types.delete_marker_replication_status.DeleteMarkerReplicationStatus"
    ]
    """<p>Indicates whether to replicate delete markers.</p> <note> <p>Indicates whether to replicate delete markers.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteMarkerReplication, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "status" in value:
        import aws_sdk_s3.types.delete_marker_replication_status

        aws_sdk_s3.types.delete_marker_replication_status.serialize_xml(
            value["status"], el, "Status"
        )


def deserialize_xml(el: Element) -> DeleteMarkerReplication:
    out: DeleteMarkerReplication = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3.types.delete_marker_replication_status

        out["status"] = (
            aws_sdk_s3.types.delete_marker_replication_status.deserialize_xml(
                child_status
            )
        )
    return out
