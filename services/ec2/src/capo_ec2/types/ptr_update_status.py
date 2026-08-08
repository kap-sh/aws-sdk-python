"""Generated from Smithy shape ``com.amazonaws.ec2#PtrUpdateStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class PtrUpdateStatus(TypedDict, closed=True):
    value: NotRequired["capo_ec2.types.string.String"]
    """<p>The value for the PTR record update.</p>"""
    status: NotRequired["capo_ec2.types.string.String"]
    """<p>The status of the PTR record update.</p>"""
    reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the PTR record update.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PtrUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "reason" in value:
        pairs.append((f"{key_prefix}Reason", str(value["reason"])))


def deserialize_ec2_query(el: Element) -> PtrUpdateStatus:
    out: PtrUpdateStatus = {}  # type: ignore[typeddict-item]
    child_value = el.find("value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    child_status = el.find("status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_reason = el.find("reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    return out
