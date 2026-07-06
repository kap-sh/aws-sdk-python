"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.policy


class GetAccessPointPolicyResult(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_s3_control.types.policy.Policy"]
    """<p>The access point policy associated with the specified access point.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetAccessPointPolicyResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "policy" in value:
        SubElement(el, "Policy").text = str(value["policy"])


def deserialize_xml(el: Element) -> GetAccessPointPolicyResult:
    out: GetAccessPointPolicyResult = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    return out
