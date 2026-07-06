"""Generated from Smithy shape ``com.amazonaws.ec2#GetVerifiedAccessGroupPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class GetVerifiedAccessGroupPolicyResult(TypedDict, closed=True):
    policy_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The status of the Verified Access policy.</p>"""
    policy_document: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Verified Access policy document.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVerifiedAccessGroupPolicyResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_enabled" in value:
        pairs.append(
            (f"{prefix}.PolicyEnabled", "true" if value["policy_enabled"] else "false")
        )
    if "policy_document" in value:
        pairs.append((f"{prefix}.PolicyDocument", str(value["policy_document"])))


def deserialize_ec2_query(el: Element) -> GetVerifiedAccessGroupPolicyResult:
    out: GetVerifiedAccessGroupPolicyResult = {}  # type: ignore[typeddict-item]
    child_policy_enabled = el.find("PolicyEnabled")
    if child_policy_enabled is not None:
        out["policy_enabled"] = (child_policy_enabled.text or "").lower() == "true"
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    return out
