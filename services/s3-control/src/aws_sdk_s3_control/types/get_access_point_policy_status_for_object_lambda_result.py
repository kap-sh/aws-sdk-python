"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointPolicyStatusForObjectLambdaResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.policy_status


class GetAccessPointPolicyStatusForObjectLambdaResult(TypedDict):
    policy_status: NotRequired["aws_sdk_s3_control.types.policy_status.PolicyStatus"]


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessPointPolicyStatusForObjectLambdaResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "policy_status" in value:
        import aws_sdk_s3_control.types.policy_status

        aws_sdk_s3_control.types.policy_status.serialize_xml(
            value["policy_status"], el, "PolicyStatus"
        )


def deserialize_xml(el: Element) -> GetAccessPointPolicyStatusForObjectLambdaResult:
    out: GetAccessPointPolicyStatusForObjectLambdaResult = {}  # type: ignore[typeddict-item]
    child_policy_status = el.find("PolicyStatus")
    if child_policy_status is not None:
        import aws_sdk_s3_control.types.policy_status

        out["policy_status"] = aws_sdk_s3_control.types.policy_status.deserialize_xml(
            child_policy_status
        )
    return out
