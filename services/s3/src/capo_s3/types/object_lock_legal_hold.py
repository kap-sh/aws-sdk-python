"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockLegalHold``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_lock_legal_hold_status


class ObjectLockLegalHold(TypedDict, closed=True):
    status: NotRequired[
        "capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus"
    ]
    """<p>Indicates whether the specified object has a legal hold in place.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectLockLegalHold, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "status" in value:
        import capo_s3.types.object_lock_legal_hold_status

        capo_s3.types.object_lock_legal_hold_status.serialize_xml(
            value["status"], el, "Status"
        )


def deserialize_xml(el: Element) -> ObjectLockLegalHold:
    out: ObjectLockLegalHold = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3.types.object_lock_legal_hold_status

        out["status"] = capo_s3.types.object_lock_legal_hold_status.deserialize_xml(
            child_status
        )
    return out
