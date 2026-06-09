"""Generated from Smithy shape ``com.amazonaws.s3#StatsEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.stats


class StatsEvent(TypedDict):
    details: NotRequired["aws_sdk_s3.types.stats.Stats"]
    """<p>The Stats event details.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StatsEvent, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "details" in value:
        import aws_sdk_s3.types.stats

        aws_sdk_s3.types.stats.serialize_xml(value["details"], el, "Details")


def deserialize_xml(el: Element) -> StatsEvent:
    out: StatsEvent = {}  # type: ignore[typeddict-item]
    child_details = el.find("Details")
    if child_details is not None:
        import aws_sdk_s3.types.stats

        out["details"] = aws_sdk_s3.types.stats.deserialize_xml(child_details)
    return out
