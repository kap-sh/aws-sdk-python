"""Generated from Smithy shape ``com.amazonaws.s3#MetadataConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.inventory_table_configuration
    import aws_sdk_s3.types.journal_table_configuration


class MetadataConfiguration(TypedDict):
    journal_table_configuration: (
        "aws_sdk_s3.types.journal_table_configuration.JournalTableConfiguration"
    )
    """<p> The journal table configuration for a metadata configuration. </p>"""
    inventory_table_configuration: NotRequired[
        "aws_sdk_s3.types.inventory_table_configuration.InventoryTableConfiguration"
    ]
    """<p> The inventory table configuration for a metadata configuration. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: MetadataConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.journal_table_configuration

    aws_sdk_s3.types.journal_table_configuration.serialize_xml(
        value["journal_table_configuration"], el, "JournalTableConfiguration"
    )
    if "inventory_table_configuration" in value:
        import aws_sdk_s3.types.inventory_table_configuration

        aws_sdk_s3.types.inventory_table_configuration.serialize_xml(
            value["inventory_table_configuration"], el, "InventoryTableConfiguration"
        )


def deserialize_xml(el: Element) -> MetadataConfiguration:
    out: MetadataConfiguration = {}  # type: ignore[typeddict-item]
    child_journal_table_configuration = el.find("JournalTableConfiguration")
    if child_journal_table_configuration is not None:
        import aws_sdk_s3.types.journal_table_configuration

        out["journal_table_configuration"] = (
            aws_sdk_s3.types.journal_table_configuration.deserialize_xml(
                child_journal_table_configuration
            )
        )
    else:
        raise DeserializationError(
            "MetadataConfiguration.journal_table_configuration required"
        )
    child_inventory_table_configuration = el.find("InventoryTableConfiguration")
    if child_inventory_table_configuration is not None:
        import aws_sdk_s3.types.inventory_table_configuration

        out["inventory_table_configuration"] = (
            aws_sdk_s3.types.inventory_table_configuration.deserialize_xml(
                child_inventory_table_configuration
            )
        )
    return out
