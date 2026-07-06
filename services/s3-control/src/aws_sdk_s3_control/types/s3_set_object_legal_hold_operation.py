"""Generated from Smithy shape ``com.amazonaws.s3control#S3SetObjectLegalHoldOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_object_lock_legal_hold


class S3SetObjectLegalHoldOperation(TypedDict, closed=True):
    legal_hold: (
        "aws_sdk_s3_control.types.s3_object_lock_legal_hold.S3ObjectLockLegalHold"
    )
    """<p>Contains the Object Lock legal hold status to be applied to all objects in the Batch Operations job.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: S3SetObjectLegalHoldOperation, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.s3_object_lock_legal_hold

    aws_sdk_s3_control.types.s3_object_lock_legal_hold.serialize_xml(
        value["legal_hold"], el, "LegalHold"
    )


def deserialize_xml(el: Element) -> S3SetObjectLegalHoldOperation:
    out: S3SetObjectLegalHoldOperation = {}  # type: ignore[typeddict-item]
    child_legal_hold = el.find("LegalHold")
    if child_legal_hold is not None:
        import aws_sdk_s3_control.types.s3_object_lock_legal_hold

        out["legal_hold"] = (
            aws_sdk_s3_control.types.s3_object_lock_legal_hold.deserialize_xml(
                child_legal_hold
            )
        )
    else:
        raise DeserializationError("S3SetObjectLegalHoldOperation.legal_hold required")
    return out
