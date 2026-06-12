"""Generated from Smithy shape ``com.amazonaws.s3control#PolicyStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.is_public


class PolicyStatus(TypedDict):
    is_public: "aws_sdk_s3_control.types.is_public.IsPublic"
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(value: PolicyStatus, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "IsPublic").text = (
        "true" if value.get("is_public", False) else "false"
    )


def deserialize_xml(el: Element) -> PolicyStatus:
    out: PolicyStatus = {}  # type: ignore[typeddict-item]
    child_is_public = el.find("IsPublic")
    if child_is_public is not None:
        out["is_public"] = (child_is_public.text or "").lower() == "true"
    else:
        out["is_public"] = False
    return out
