"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#CreateSlotTypeVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.custom_or_builtin_slot_type_name
    import aws_sdk_lex_model_building_service.types.description
    import aws_sdk_lex_model_building_service.types.enumeration_values
    import aws_sdk_lex_model_building_service.types.slot_type_configurations
    import aws_sdk_lex_model_building_service.types.slot_type_name
    import aws_sdk_lex_model_building_service.types.slot_value_selection_strategy
    import aws_sdk_lex_model_building_service.types.string
    import aws_sdk_lex_model_building_service.types.timestamp
    import aws_sdk_lex_model_building_service.types.version


class CreateSlotTypeVersionResponse(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_lex_model_building_service.types.slot_type_name.SlotTypeName"
    ]
    """<p>The name of the slot type.</p>"""
    description: NotRequired[
        "aws_sdk_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the slot type.</p>"""
    enumeration_values: NotRequired[
        "aws_sdk_lex_model_building_service.types.enumeration_values.EnumerationValues"
    ]
    """<p>A list of <code>EnumerationValue</code> objects that defines the values that the slot type can take.</p>"""
    last_updated_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the slot type was updated. When you create a resource, the creation date and last update date are the same.</p>"""
    created_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the slot type was created.</p>"""
    version: NotRequired["aws_sdk_lex_model_building_service.types.version.Version"]
    """<p>The version assigned to the new slot type version. </p>"""
    checksum: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]
    """<p>Checksum of the <code>$LATEST</code> version of the slot type.</p>"""
    value_selection_strategy: NotRequired[
        "aws_sdk_lex_model_building_service.types.slot_value_selection_strategy.SlotValueSelectionStrategy"
    ]
    """<p>The strategy that Amazon Lex uses to determine the value of the slot. For more information, see <a>PutSlotType</a>.</p>"""
    parent_slot_type_signature: NotRequired[
        "aws_sdk_lex_model_building_service.types.custom_or_builtin_slot_type_name.CustomOrBuiltinSlotTypeName"
    ]
    """<p>The built-in slot type used a the parent of the slot type.</p>"""
    slot_type_configurations: NotRequired[
        "aws_sdk_lex_model_building_service.types.slot_type_configurations.SlotTypeConfigurations"
    ]
    """<p>Configuration information that extends the parent built-in slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSlotTypeVersionResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "enumeration_values" in value:
        import aws_sdk_lex_model_building_service.types.enumeration_values

        out["enumerationValues"] = (
            aws_sdk_lex_model_building_service.types.enumeration_values.serialize_json(
                value["enumeration_values"]
            )
        )
    if "last_updated_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["lastUpdatedDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "created_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    if "value_selection_strategy" in value:
        import aws_sdk_lex_model_building_service.types.slot_value_selection_strategy

        out["valueSelectionStrategy"] = (
            aws_sdk_lex_model_building_service.types.slot_value_selection_strategy.serialize_json(
                value["value_selection_strategy"]
            )
        )
    if "parent_slot_type_signature" in value:
        out["parentSlotTypeSignature"] = value["parent_slot_type_signature"]
    if "slot_type_configurations" in value:
        import aws_sdk_lex_model_building_service.types.slot_type_configurations

        out["slotTypeConfigurations"] = (
            aws_sdk_lex_model_building_service.types.slot_type_configurations.serialize_json(
                value["slot_type_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSlotTypeVersionResponse:
    out: CreateSlotTypeVersionResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "enumerationValues" in data:
        import aws_sdk_lex_model_building_service.types.enumeration_values

        out["enumeration_values"] = (
            aws_sdk_lex_model_building_service.types.enumeration_values.deserialize_json(
                data["enumerationValues"]
            )
        )
    if "lastUpdatedDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["last_updated_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "createdDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["created_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    if "valueSelectionStrategy" in data:
        import aws_sdk_lex_model_building_service.types.slot_value_selection_strategy

        out["value_selection_strategy"] = (
            aws_sdk_lex_model_building_service.types.slot_value_selection_strategy.deserialize_json(
                data["valueSelectionStrategy"]
            )
        )
    if "parentSlotTypeSignature" in data:
        out["parent_slot_type_signature"] = data["parentSlotTypeSignature"]
    if "slotTypeConfigurations" in data:
        import aws_sdk_lex_model_building_service.types.slot_type_configurations

        out["slot_type_configurations"] = (
            aws_sdk_lex_model_building_service.types.slot_type_configurations.deserialize_json(
                data["slotTypeConfigurations"]
            )
        )
    return out
