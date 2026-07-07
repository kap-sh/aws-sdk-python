"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointPolicyStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.policy_status


class GetAccessPointPolicyStatusResult(TypedDict, closed=True):
    policy_status: NotRequired["aws_sdk_s3_control.types.policy_status.PolicyStatus"]
    """<p>Indicates the current policy status of the specified access point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessPointPolicyStatusResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "policy_status" in value:
        import aws_sdk_s3_control.types.policy_status

        aws_sdk_s3_control.types.policy_status.serialize_xml(
            value["policy_status"], el, "PolicyStatus"
        )


def deserialize_xml(el: Element) -> GetAccessPointPolicyStatusResult:
    out: GetAccessPointPolicyStatusResult = {}  # type: ignore[typeddict-item]
    child_policy_status = el.find("PolicyStatus")
    if child_policy_status is not None:
        import aws_sdk_s3_control.types.policy_status

        out["policy_status"] = aws_sdk_s3_control.types.policy_status.deserialize_xml(
            child_policy_status
        )
    return out
