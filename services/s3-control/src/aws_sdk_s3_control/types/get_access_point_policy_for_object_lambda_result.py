"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointPolicyForObjectLambdaResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.object_lambda_policy


class GetAccessPointPolicyForObjectLambdaResult(TypedDict):
    policy: NotRequired[
        "aws_sdk_s3_control.types.object_lambda_policy.ObjectLambdaPolicy"
    ]
    """<p>Object Lambda Access Point resource policy document.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessPointPolicyForObjectLambdaResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "policy" in value:
        SubElement(el, "Policy").text = str(value["policy"])


def deserialize_xml(el: Element) -> GetAccessPointPolicyForObjectLambdaResult:
    out: GetAccessPointPolicyForObjectLambdaResult = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    return out
