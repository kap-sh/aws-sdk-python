"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockLegalHold``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_object_lock_legal_hold_status


class S3ObjectLockLegalHold(TypedDict):
    status: "aws_sdk_s3_control.types.s3_object_lock_legal_hold_status.S3ObjectLockLegalHoldStatus"
    """<p>The Object Lock legal hold status to be applied to all objects in the Batch Operations job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3ObjectLockLegalHold, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.s3_object_lock_legal_hold_status

    aws_sdk_s3_control.types.s3_object_lock_legal_hold_status.serialize_xml(
        value["status"], el, "Status"
    )


def deserialize_xml(el: Element) -> S3ObjectLockLegalHold:
    out: S3ObjectLockLegalHold = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3_control.types.s3_object_lock_legal_hold_status

        out["status"] = (
            aws_sdk_s3_control.types.s3_object_lock_legal_hold_status.deserialize_xml(
                child_status
            )
        )
    else:
        raise DeserializationError("S3ObjectLockLegalHold.status required")
    return out
