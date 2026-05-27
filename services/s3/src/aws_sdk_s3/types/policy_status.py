"""Generated from Smithy shape ``com.amazonaws.s3#PolicyStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.is_public


class PolicyStatus(TypedDict):
    is_public: NotRequired["aws_sdk_s3.types.is_public.IsPublic"]
    """<p>The policy status for this bucket. <code>TRUE</code> indicates that this bucket is public. <code>FALSE</code> indicates that the bucket is not public.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PolicyStatus, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "is_public" in value:
        SubElement(el, "IsPublic").text = "true" if value["is_public"] else "false"


def deserialize_xml(el: Element) -> PolicyStatus:
    out: PolicyStatus = {}  # type: ignore[typeddict-item]
    child_is_public = el.find("IsPublic")
    if child_is_public is not None:
        out["is_public"] = (child_is_public.text or "").lower() == "true"
    return out
