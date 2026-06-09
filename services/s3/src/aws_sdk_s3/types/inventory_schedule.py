"""Generated from Smithy shape ``com.amazonaws.s3#InventorySchedule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.inventory_frequency


class InventorySchedule(TypedDict):
    frequency: "aws_sdk_s3.types.inventory_frequency.InventoryFrequency"
    """<p>Specifies how frequently inventory results are produced.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InventorySchedule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.inventory_frequency

    aws_sdk_s3.types.inventory_frequency.serialize_xml(
        value["frequency"], el, "Frequency"
    )


def deserialize_xml(el: Element) -> InventorySchedule:
    out: InventorySchedule = {}  # type: ignore[typeddict-item]
    child_frequency = el.find("Frequency")
    if child_frequency is not None:
        import aws_sdk_s3.types.inventory_frequency

        out["frequency"] = aws_sdk_s3.types.inventory_frequency.deserialize_xml(
            child_frequency
        )
    else:
        raise DeserializationError("InventorySchedule.frequency required")
    return out
