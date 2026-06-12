"""Generated from Smithy shape ``com.amazonaws.s3control#SelectionCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.min_storage_bytes_percentage
    import aws_sdk_s3_control.types.storage_lens_prefix_level_delimiter
    import aws_sdk_s3_control.types.storage_lens_prefix_level_max_depth


class SelectionCriteria(TypedDict):
    delimiter: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_prefix_level_delimiter.StorageLensPrefixLevelDelimiter"
    ]
    """<p>A container for the delimiter of the selection criteria being used.</p>"""
    max_depth: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_prefix_level_max_depth.StorageLensPrefixLevelMaxDepth"
    ]
    """<p>The max depth of the selection criteria</p>"""
    min_storage_bytes_percentage: NotRequired[
        "aws_sdk_s3_control.types.min_storage_bytes_percentage.MinStorageBytesPercentage"
    ]
    """<p>The minimum number of storage bytes percentage whose metrics will be selected.</p> <note> <p>You must choose a value greater than or equal to <code>1.0</code>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: SelectionCriteria, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "delimiter" in value:
        SubElement(el, "Delimiter").text = str(value["delimiter"])
    if "max_depth" in value:
        SubElement(el, "MaxDepth").text = str(value["max_depth"])
    if "min_storage_bytes_percentage" in value:
        SubElement(el, "MinStorageBytesPercentage").text = str(
            value["min_storage_bytes_percentage"]
        )


def deserialize_xml(el: Element) -> SelectionCriteria:
    out: SelectionCriteria = {}  # type: ignore[typeddict-item]
    child_delimiter = el.find("Delimiter")
    if child_delimiter is not None:
        out["delimiter"] = str(child_delimiter.text or "")
    child_max_depth = el.find("MaxDepth")
    if child_max_depth is not None:
        out["max_depth"] = int(child_max_depth.text or "")
    child_min_storage_bytes_percentage = el.find("MinStorageBytesPercentage")
    if child_min_storage_bytes_percentage is not None:
        out["min_storage_bytes_percentage"] = float(
            child_min_storage_bytes_percentage.text or ""
        )
    return out
