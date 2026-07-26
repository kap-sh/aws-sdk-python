"""Generated from Smithy shape ``com.amazonaws.s3#NotificationConfigurationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.s3_key_filter


class NotificationConfigurationFilter(TypedDict, closed=True):
    key: NotRequired["capo_s3.types.s3_key_filter.S3KeyFilter"]


# --- restXml ser/de ---
def serialize_xml(
    value: NotificationConfigurationFilter, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "key" in value:
        import capo_s3.types.s3_key_filter

        capo_s3.types.s3_key_filter.serialize_xml(value["key"], el, "S3Key")


def deserialize_xml(el: Element) -> NotificationConfigurationFilter:
    out: NotificationConfigurationFilter = {}  # type: ignore[typeddict-item]
    child_key = el.find("S3Key")
    if child_key is not None:
        import capo_s3.types.s3_key_filter

        out["key"] = capo_s3.types.s3_key_filter.deserialize_xml(child_key)
    return out
