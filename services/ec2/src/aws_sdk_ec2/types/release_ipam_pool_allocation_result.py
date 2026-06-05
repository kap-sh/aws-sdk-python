"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseIpamPoolAllocationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class ReleaseIpamPoolAllocationResult(TypedDict):
    success: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates if the release was successful.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReleaseIpamPoolAllocationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "success" in value:
        pairs.append((f"{prefix}.Success", "true" if value["success"] else "false"))


def deserialize_ec2_query(el: Element) -> ReleaseIpamPoolAllocationResult:
    out: ReleaseIpamPoolAllocationResult = {}  # type: ignore[typeddict-item]
    child_success = el.find("Success")
    if child_success is not None:
        out["success"] = (child_success.text or "").lower() == "true"
    return out
