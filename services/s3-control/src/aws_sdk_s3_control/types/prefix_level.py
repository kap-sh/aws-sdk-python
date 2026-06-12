"""Generated from Smithy shape ``com.amazonaws.s3control#PrefixLevel``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.prefix_level_storage_metrics


class PrefixLevel(TypedDict):
    storage_metrics: "aws_sdk_s3_control.types.prefix_level_storage_metrics.PrefixLevelStorageMetrics"
    """<p>A container for the prefix-level storage metrics for S3 Storage Lens.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PrefixLevel, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.prefix_level_storage_metrics

    aws_sdk_s3_control.types.prefix_level_storage_metrics.serialize_xml(
        value["storage_metrics"], el, "StorageMetrics"
    )


def deserialize_xml(el: Element) -> PrefixLevel:
    out: PrefixLevel = {}  # type: ignore[typeddict-item]
    child_storage_metrics = el.find("StorageMetrics")
    if child_storage_metrics is not None:
        import aws_sdk_s3_control.types.prefix_level_storage_metrics

        out["storage_metrics"] = (
            aws_sdk_s3_control.types.prefix_level_storage_metrics.deserialize_xml(
                child_storage_metrics
            )
        )
    else:
        raise DeserializationError("PrefixLevel.storage_metrics required")
    return out
