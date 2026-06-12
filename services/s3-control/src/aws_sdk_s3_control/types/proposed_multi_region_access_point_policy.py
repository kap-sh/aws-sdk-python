"""Generated from Smithy shape ``com.amazonaws.s3control#ProposedMultiRegionAccessPointPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.policy


class ProposedMultiRegionAccessPointPolicy(TypedDict):
    policy: NotRequired["aws_sdk_s3_control.types.policy.Policy"]
    """<p>The details of the proposed policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ProposedMultiRegionAccessPointPolicy, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "policy" in value:
        SubElement(el, "Policy").text = str(value["policy"])


def deserialize_xml(el: Element) -> ProposedMultiRegionAccessPointPolicy:
    out: ProposedMultiRegionAccessPointPolicy = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    return out
