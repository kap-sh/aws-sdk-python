"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectLegalHoldOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_lock_legal_hold


class GetObjectLegalHoldOutput(TypedDict, closed=True):
    legal_hold: NotRequired["capo_s3.types.object_lock_legal_hold.ObjectLockLegalHold"]
    """<p>The current legal hold status for the specified object.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetObjectLegalHoldOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "legal_hold" in value:
        import capo_s3.types.object_lock_legal_hold

        capo_s3.types.object_lock_legal_hold.serialize_xml(
            value["legal_hold"], el, "LegalHold"
        )


def deserialize_xml(el: Element) -> GetObjectLegalHoldOutput:
    out: GetObjectLegalHoldOutput = {}  # type: ignore[typeddict-item]
    child_legal_hold = el.find("LegalHold")
    if child_legal_hold is not None:
        import capo_s3.types.object_lock_legal_hold

        out["legal_hold"] = capo_s3.types.object_lock_legal_hold.deserialize_xml(
            child_legal_hold
        )
    return out
