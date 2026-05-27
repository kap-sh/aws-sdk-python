"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketPolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.policy


class GetBucketPolicyOutput(TypedDict):
    policy: NotRequired["aws_sdk_s3.types.policy.Policy"]
    """<p>The bucket policy as a JSON document.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketPolicyOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "policy" in value:
        SubElement(el, "Policy").text = str(value["policy"])


def deserialize_xml(el: Element) -> GetBucketPolicyOutput:
    out: GetBucketPolicyOutput = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    return out
