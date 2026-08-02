"""Generated from Smithy shape ``com.amazonaws.ec2#GetEnabledIpamPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_policy_id
    import capo_ec2.types.ipam_policy_managed_by


class GetEnabledIpamPolicyResult(TypedDict, closed=True):
    ipam_policy_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the IPAM policy is enabled.</p>"""
    ipam_policy_id: NotRequired["capo_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the enabled IPAM policy.</p>"""
    managed_by: NotRequired["capo_ec2.types.ipam_policy_managed_by.IpamPolicyManagedBy"]
    """<p>The entity that manages the IPAM policy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetEnabledIpamPolicyResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_policy_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPolicyEnabled",
                "true" if value["ipam_policy_enabled"] else "false",
            )
        )
    if "ipam_policy_id" in value:
        pairs.append((f"{key_prefix}IpamPolicyId", str(value["ipam_policy_id"])))
    if "managed_by" in value:
        import capo_ec2.types.ipam_policy_managed_by

        capo_ec2.types.ipam_policy_managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{key_prefix}ManagedBy"
        )


def deserialize_ec2_query(el: Element) -> GetEnabledIpamPolicyResult:
    out: GetEnabledIpamPolicyResult = {}  # type: ignore[typeddict-item]
    child_ipam_policy_enabled = el.find("IpamPolicyEnabled")
    if child_ipam_policy_enabled is not None:
        out["ipam_policy_enabled"] = (
            child_ipam_policy_enabled.text or ""
        ).lower() == "true"
    child_ipam_policy_id = el.find("IpamPolicyId")
    if child_ipam_policy_id is not None:
        out["ipam_policy_id"] = str(child_ipam_policy_id.text or "")
    child_managed_by = el.find("ManagedBy")
    if child_managed_by is not None:
        import capo_ec2.types.ipam_policy_managed_by

        out["managed_by"] = capo_ec2.types.ipam_policy_managed_by.deserialize_ec2_query(
            child_managed_by
        )
    return out
