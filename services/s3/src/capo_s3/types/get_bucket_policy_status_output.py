"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketPolicyStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.policy_status


class GetBucketPolicyStatusOutput(TypedDict, closed=True):
    policy_status: NotRequired["capo_s3.types.policy_status.PolicyStatus"]
    """<p>The policy status for the specified bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketPolicyStatusOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "policy_status" in value:
        import capo_s3.types.policy_status

        capo_s3.types.policy_status.serialize_xml(
            value["policy_status"], el, "PolicyStatus"
        )


def deserialize_xml(el: Element) -> GetBucketPolicyStatusOutput:
    out: GetBucketPolicyStatusOutput = {}  # type: ignore[typeddict-item]
    child_policy_status = el.find("PolicyStatus")
    if child_policy_status is not None:
        import capo_s3.types.policy_status

        out["policy_status"] = capo_s3.types.policy_status.deserialize_xml(
            child_policy_status
        )
    return out
