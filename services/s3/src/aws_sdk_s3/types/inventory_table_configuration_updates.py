"""Generated from Smithy shape ``com.amazonaws.s3#InventoryTableConfigurationUpdates``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.inventory_configuration_state
    import aws_sdk_s3.types.metadata_table_encryption_configuration


class InventoryTableConfigurationUpdates(TypedDict):
    configuration_state: (
        "aws_sdk_s3.types.inventory_configuration_state.InventoryConfigurationState"
    )
    """<p> The configuration state of the inventory table, indicating whether the inventory table is enabled or disabled. </p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_s3.types.metadata_table_encryption_configuration.MetadataTableEncryptionConfiguration"
    ]
    """<p> The encryption configuration for the inventory table. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: InventoryTableConfigurationUpdates, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.inventory_configuration_state

    aws_sdk_s3.types.inventory_configuration_state.serialize_xml(
        value["configuration_state"], el, "ConfigurationState"
    )
    if "encryption_configuration" in value:
        import aws_sdk_s3.types.metadata_table_encryption_configuration

        aws_sdk_s3.types.metadata_table_encryption_configuration.serialize_xml(
            value["encryption_configuration"], el, "EncryptionConfiguration"
        )


def deserialize_xml(el: Element) -> InventoryTableConfigurationUpdates:
    out: InventoryTableConfigurationUpdates = {}  # type: ignore[typeddict-item]
    child_configuration_state = el.find("ConfigurationState")
    if child_configuration_state is not None:
        import aws_sdk_s3.types.inventory_configuration_state

        out["configuration_state"] = (
            aws_sdk_s3.types.inventory_configuration_state.deserialize_xml(
                child_configuration_state
            )
        )
    else:
        raise DeserializationError(
            "InventoryTableConfigurationUpdates.configuration_state required"
        )
    child_encryption_configuration = el.find("EncryptionConfiguration")
    if child_encryption_configuration is not None:
        import aws_sdk_s3.types.metadata_table_encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_s3.types.metadata_table_encryption_configuration.deserialize_xml(
                child_encryption_configuration
            )
        )
    return out
