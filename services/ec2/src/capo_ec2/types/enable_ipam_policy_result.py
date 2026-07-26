"""Generated from Smithy shape ``com.amazonaws.ec2#EnableIpamPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_id


class EnableIpamPolicyResult(TypedDict, closed=True):
    ipam_policy_id: NotRequired["capo_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy that was enabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableIpamPolicyResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_policy_id" in value:
        pairs.append((f"{prefix}.IpamPolicyId", str(value["ipam_policy_id"])))


def deserialize_ec2_query(el: Element) -> EnableIpamPolicyResult:
    out: EnableIpamPolicyResult = {}  # type: ignore[typeddict-item]
    child_ipam_policy_id = el.find("IpamPolicyId")
    if child_ipam_policy_id is not None:
        out["ipam_policy_id"] = str(child_ipam_policy_id.text or "")
    return out
