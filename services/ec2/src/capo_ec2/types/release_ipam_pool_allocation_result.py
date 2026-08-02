"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseIpamPoolAllocationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class ReleaseIpamPoolAllocationResult(TypedDict, closed=True):
    success: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates if the release was successful.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReleaseIpamPoolAllocationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "success" in value:
        pairs.append((f"{key_prefix}Success", "true" if value["success"] else "false"))


def deserialize_ec2_query(el: Element) -> ReleaseIpamPoolAllocationResult:
    out: ReleaseIpamPoolAllocationResult = {}  # type: ignore[typeddict-item]
    child_success = el.find("Success")
    if child_success is not None:
        out["success"] = (child_success.text or "").lower() == "true"
    return out
