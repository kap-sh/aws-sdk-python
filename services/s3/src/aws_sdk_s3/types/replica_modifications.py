"""Generated from Smithy shape ``com.amazonaws.s3#ReplicaModifications``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.replica_modifications_status


class ReplicaModifications(TypedDict):
    status: "aws_sdk_s3.types.replica_modifications_status.ReplicaModificationsStatus"
    """<p>Specifies whether Amazon S3 replicates modifications on replicas.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReplicaModifications, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.replica_modifications_status

    aws_sdk_s3.types.replica_modifications_status.serialize_xml(
        value["status"], el, "Status"
    )


def deserialize_xml(el: Element) -> ReplicaModifications:
    out: ReplicaModifications = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3.types.replica_modifications_status

        out["status"] = aws_sdk_s3.types.replica_modifications_status.deserialize_xml(
            child_status
        )
    else:
        raise DeserializationError("ReplicaModifications.status required")
    return out
