"""Generated from Smithy shape ``com.amazonaws.s3#MetadataConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.annotation_table_configuration_result
    import capo_s3.types.destination_result
    import capo_s3.types.inventory_table_configuration_result
    import capo_s3.types.journal_table_configuration_result


class MetadataConfigurationResult(TypedDict, closed=True):
    destination_result: "capo_s3.types.destination_result.DestinationResult"
    """<p> The destination settings for a metadata configuration. </p>"""
    journal_table_configuration_result: NotRequired[
        "capo_s3.types.journal_table_configuration_result.JournalTableConfigurationResult"
    ]
    """<p> The journal table configuration for a metadata configuration. </p>"""
    inventory_table_configuration_result: NotRequired[
        "capo_s3.types.inventory_table_configuration_result.InventoryTableConfigurationResult"
    ]
    """<p> The inventory table configuration for a metadata configuration. </p>"""
    annotation_table_configuration_result: NotRequired[
        "capo_s3.types.annotation_table_configuration_result.AnnotationTableConfigurationResult"
    ]
    """<p>The annotation table configuration result, if an annotation table is configured.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: MetadataConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.destination_result

    capo_s3.types.destination_result.serialize_xml(
        value["destination_result"], el, "DestinationResult"
    )
    if "journal_table_configuration_result" in value:
        import capo_s3.types.journal_table_configuration_result

        capo_s3.types.journal_table_configuration_result.serialize_xml(
            value["journal_table_configuration_result"],
            el,
            "JournalTableConfigurationResult",
        )
    if "inventory_table_configuration_result" in value:
        import capo_s3.types.inventory_table_configuration_result

        capo_s3.types.inventory_table_configuration_result.serialize_xml(
            value["inventory_table_configuration_result"],
            el,
            "InventoryTableConfigurationResult",
        )
    if "annotation_table_configuration_result" in value:
        import capo_s3.types.annotation_table_configuration_result

        capo_s3.types.annotation_table_configuration_result.serialize_xml(
            value["annotation_table_configuration_result"],
            el,
            "AnnotationTableConfigurationResult",
        )


def deserialize_xml(el: Element) -> MetadataConfigurationResult:
    out: MetadataConfigurationResult = {}  # type: ignore[typeddict-item]
    child_destination_result = el.find("DestinationResult")
    if child_destination_result is not None:
        import capo_s3.types.destination_result

        out["destination_result"] = capo_s3.types.destination_result.deserialize_xml(
            child_destination_result
        )
    else:
        raise DeserializationError(
            "MetadataConfigurationResult.destination_result required"
        )
    child_journal_table_configuration_result = el.find(
        "JournalTableConfigurationResult"
    )
    if child_journal_table_configuration_result is not None:
        import capo_s3.types.journal_table_configuration_result

        out["journal_table_configuration_result"] = (
            capo_s3.types.journal_table_configuration_result.deserialize_xml(
                child_journal_table_configuration_result
            )
        )
    child_inventory_table_configuration_result = el.find(
        "InventoryTableConfigurationResult"
    )
    if child_inventory_table_configuration_result is not None:
        import capo_s3.types.inventory_table_configuration_result

        out["inventory_table_configuration_result"] = (
            capo_s3.types.inventory_table_configuration_result.deserialize_xml(
                child_inventory_table_configuration_result
            )
        )
    child_annotation_table_configuration_result = el.find(
        "AnnotationTableConfigurationResult"
    )
    if child_annotation_table_configuration_result is not None:
        import capo_s3.types.annotation_table_configuration_result

        out["annotation_table_configuration_result"] = (
            capo_s3.types.annotation_table_configuration_result.deserialize_xml(
                child_annotation_table_configuration_result
            )
        )
    return out
