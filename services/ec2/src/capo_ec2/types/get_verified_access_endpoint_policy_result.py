"""Generated from Smithy shape ``com.amazonaws.ec2#GetVerifiedAccessEndpointPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class GetVerifiedAccessEndpointPolicyResult(TypedDict, closed=True):
    policy_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>The status of the Verified Access policy.</p>"""
    policy_document: NotRequired["capo_ec2.types.string.String"]
    """<p>The Verified Access policy document.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVerifiedAccessEndpointPolicyResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}PolicyEnabled",
                "true" if value["policy_enabled"] else "false",
            )
        )
    if "policy_document" in value:
        pairs.append((f"{key_prefix}PolicyDocument", str(value["policy_document"])))


def deserialize_ec2_query(el: Element) -> GetVerifiedAccessEndpointPolicyResult:
    out: GetVerifiedAccessEndpointPolicyResult = {}  # type: ignore[typeddict-item]
    child_policy_enabled = el.find("policyEnabled")
    if child_policy_enabled is not None:
        out["policy_enabled"] = (child_policy_enabled.text or "").lower() == "true"
    child_policy_document = el.find("policyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    return out
