"""Generated from Smithy shape ``com.amazonaws.s3#SseKmsEncryptedObjects``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.sse_kms_encrypted_objects_status


class SseKmsEncryptedObjects(TypedDict, closed=True):
    status: (
        "aws_sdk_s3.types.sse_kms_encrypted_objects_status.SseKmsEncryptedObjectsStatus"
    )
    """<p>Specifies whether Amazon S3 replicates objects created with server-side encryption using an Amazon Web Services KMS key stored in Amazon Web Services Key Management Service.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: SseKmsEncryptedObjects, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.sse_kms_encrypted_objects_status

    aws_sdk_s3.types.sse_kms_encrypted_objects_status.serialize_xml(
        value["status"], el, "Status"
    )


def deserialize_xml(el: Element) -> SseKmsEncryptedObjects:
    out: SseKmsEncryptedObjects = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3.types.sse_kms_encrypted_objects_status

        out["status"] = (
            aws_sdk_s3.types.sse_kms_encrypted_objects_status.deserialize_xml(
                child_status
            )
        )
    else:
        raise DeserializationError("SseKmsEncryptedObjects.status required")
    return out
