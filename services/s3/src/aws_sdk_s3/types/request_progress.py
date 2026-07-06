"""Generated from Smithy shape ``com.amazonaws.s3#RequestProgress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.enable_request_progress


class RequestProgress(TypedDict, closed=True):
    enabled: NotRequired[
        "aws_sdk_s3.types.enable_request_progress.EnableRequestProgress"
    ]
    """<p>Specifies whether periodic QueryProgress frames should be sent. Valid values: TRUE, FALSE. Default value: FALSE.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RequestProgress, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "enabled" in value:
        SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"


def deserialize_xml(el: Element) -> RequestProgress:
    out: RequestProgress = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
