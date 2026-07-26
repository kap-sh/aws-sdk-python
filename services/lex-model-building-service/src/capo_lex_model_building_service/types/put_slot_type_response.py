"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#PutSlotTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.boolean
    import capo_lex_model_building_service.types.custom_or_builtin_slot_type_name
    import capo_lex_model_building_service.types.description
    import capo_lex_model_building_service.types.enumeration_values
    import capo_lex_model_building_service.types.slot_type_configurations
    import capo_lex_model_building_service.types.slot_type_name
    import capo_lex_model_building_service.types.slot_value_selection_strategy
    import capo_lex_model_building_service.types.string
    import capo_lex_model_building_service.types.timestamp
    import capo_lex_model_building_service.types.version


class PutSlotTypeResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_lex_model_building_service.types.slot_type_name.SlotTypeName"
    ]
    """<p>The name of the slot type.</p>"""
    description: NotRequired[
        "capo_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the slot type.</p>"""
    enumeration_values: NotRequired[
        "capo_lex_model_building_service.types.enumeration_values.EnumerationValues"
    ]
    """<p>A list of <code>EnumerationValue</code> objects that defines the values that the slot type can take.</p>"""
    last_updated_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the slot type was updated. When you create a slot type, the creation date and last update date are the same.</p>"""
    created_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the slot type was created.</p>"""
    version: NotRequired["capo_lex_model_building_service.types.version.Version"]
    """<p>The version of the slot type. For a new slot type, the version is always <code>$LATEST</code>. </p>"""
    checksum: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>Checksum of the <code>$LATEST</code> version of the slot type.</p>"""
    value_selection_strategy: NotRequired[
        "capo_lex_model_building_service.types.slot_value_selection_strategy.SlotValueSelectionStrategy"
    ]
    """<p>The slot resolution strategy that Amazon Lex uses to determine the value of the slot. For more information, see <a>PutSlotType</a>.</p>"""
    create_version: NotRequired["capo_lex_model_building_service.types.boolean.Boolean"]
    """<p> <code>True</code> if a new version of the slot type was created. If the <code>createVersion</code> field was not specified in the request, the <code>createVersion</code> field is set to false in the response.</p>"""
    parent_slot_type_signature: NotRequired[
        "capo_lex_model_building_service.types.custom_or_builtin_slot_type_name.CustomOrBuiltinSlotTypeName"
    ]
    """<p>The built-in slot type used as the parent of the slot type.</p>"""
    slot_type_configurations: NotRequired[
        "capo_lex_model_building_service.types.slot_type_configurations.SlotTypeConfigurations"
    ]
    """<p>Configuration information that extends the parent built-in slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSlotTypeResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "enumeration_values" in value:
        import capo_lex_model_building_service.types.enumeration_values

        out["enumerationValues"] = (
            capo_lex_model_building_service.types.enumeration_values.serialize_json(
                value["enumeration_values"]
            )
        )
    if "last_updated_date" in value:
        import capo_lex_model_building_service.types.timestamp

        out["lastUpdatedDate"] = (
            capo_lex_model_building_service.types.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "created_date" in value:
        import capo_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            capo_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    if "value_selection_strategy" in value:
        import capo_lex_model_building_service.types.slot_value_selection_strategy

        out["valueSelectionStrategy"] = (
            capo_lex_model_building_service.types.slot_value_selection_strategy.serialize_json(
                value["value_selection_strategy"]
            )
        )
    if "create_version" in value:
        out["createVersion"] = value["create_version"]
    if "parent_slot_type_signature" in value:
        out["parentSlotTypeSignature"] = value["parent_slot_type_signature"]
    if "slot_type_configurations" in value:
        import capo_lex_model_building_service.types.slot_type_configurations

        out["slotTypeConfigurations"] = (
            capo_lex_model_building_service.types.slot_type_configurations.serialize_json(
                value["slot_type_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutSlotTypeResponse:
    out: PutSlotTypeResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "enumerationValues" in data:
        import capo_lex_model_building_service.types.enumeration_values

        out["enumeration_values"] = (
            capo_lex_model_building_service.types.enumeration_values.deserialize_json(
                data["enumerationValues"]
            )
        )
    if "lastUpdatedDate" in data:
        import capo_lex_model_building_service.types.timestamp

        out["last_updated_date"] = (
            capo_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "createdDate" in data:
        import capo_lex_model_building_service.types.timestamp

        out["created_date"] = (
            capo_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    if "valueSelectionStrategy" in data:
        import capo_lex_model_building_service.types.slot_value_selection_strategy

        out["value_selection_strategy"] = (
            capo_lex_model_building_service.types.slot_value_selection_strategy.deserialize_json(
                data["valueSelectionStrategy"]
            )
        )
    if "createVersion" in data:
        out["create_version"] = data["createVersion"]
    if "parentSlotTypeSignature" in data:
        out["parent_slot_type_signature"] = data["parentSlotTypeSignature"]
    if "slotTypeConfigurations" in data:
        import capo_lex_model_building_service.types.slot_type_configurations

        out["slot_type_configurations"] = (
            capo_lex_model_building_service.types.slot_type_configurations.deserialize_json(
                data["slotTypeConfigurations"]
            )
        )
    return out
