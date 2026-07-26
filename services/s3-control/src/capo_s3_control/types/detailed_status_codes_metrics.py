"""Generated from Smithy shape ``com.amazonaws.s3control#DetailedStatusCodesMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.is_enabled


class DetailedStatusCodesMetrics(TypedDict, closed=True):
    is_enabled: "capo_s3_control.types.is_enabled.IsEnabled"
    """<p>A container that indicates whether detailed status code metrics are enabled.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DetailedStatusCodesMetrics, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "IsEnabled").text = (
        "true" if value.get("is_enabled", False) else "false"
    )


def deserialize_xml(el: Element) -> DetailedStatusCodesMetrics:
    out: DetailedStatusCodesMetrics = {}  # type: ignore[typeddict-item]
    child_is_enabled = el.find("IsEnabled")
    if child_is_enabled is not None:
        out["is_enabled"] = (child_is_enabled.text or "").lower() == "true"
    else:
        out["is_enabled"] = False
    return out
