"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectLegalHoldOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.object_lock_legal_hold


class GetObjectLegalHoldOutput(TypedDict):
    legal_hold: NotRequired[
        "aws_sdk_s3.types.object_lock_legal_hold.ObjectLockLegalHold"
    ]
    """<p>The current legal hold status for the specified object.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetObjectLegalHoldOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "legal_hold" in value:
        import aws_sdk_s3.types.object_lock_legal_hold

        aws_sdk_s3.types.object_lock_legal_hold.serialize_xml(
            value["legal_hold"], el, "LegalHold"
        )


def deserialize_xml(el: Element) -> GetObjectLegalHoldOutput:
    out: GetObjectLegalHoldOutput = {}  # type: ignore[typeddict-item]
    child_legal_hold = el.find("LegalHold")
    if child_legal_hold is not None:
        import aws_sdk_s3.types.object_lock_legal_hold

        out["legal_hold"] = aws_sdk_s3.types.object_lock_legal_hold.deserialize_xml(
            child_legal_hold
        )
    return out
