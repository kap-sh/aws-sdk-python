"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateSlotTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.composite_slot_type_setting
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.external_source_setting
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.slot_type_signature
    import capo_lex_models_v2.types.slot_type_values
    import capo_lex_models_v2.types.slot_value_selection_setting
    import capo_lex_models_v2.types.timestamp


class UpdateSlotTypeResponse(TypedDict, closed=True):
    slot_type_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the updated slot type.</p>"""
    slot_type_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The updated name of the slot type.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The updated description of the slot type.</p>"""
    slot_type_values: NotRequired[
        "capo_lex_models_v2.types.slot_type_values.SlotTypeValues"
    ]
    """<p>The updated values that the slot type provides.</p>"""
    value_selection_setting: NotRequired[
        "capo_lex_models_v2.types.slot_value_selection_setting.SlotValueSelectionSetting"
    ]
    """<p>The updated strategy that Amazon Lex uses to determine which value to select from the slot type.</p>"""
    parent_slot_type_signature: NotRequired[
        "capo_lex_models_v2.types.slot_type_signature.SlotTypeSignature"
    ]
    """<p>The updated signature of the built-in slot type that is the parent of this slot type.</p>"""
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that contains the slot type.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that contains the slot type. This is always <code>DRAFT</code>.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The language and locale of the updated slot type.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The timestamp of the date and time that the slot type was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the slot type was last updated.</p>"""
    external_source_setting: NotRequired[
        "capo_lex_models_v2.types.external_source_setting.ExternalSourceSetting"
    ]
    composite_slot_type_setting: NotRequired[
        "capo_lex_models_v2.types.composite_slot_type_setting.CompositeSlotTypeSetting"
    ]
    """<p>Specifications for a composite slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSlotTypeResponse) -> dict:
    out: dict = {}
    if "slot_type_id" in value:
        out["slotTypeId"] = value["slot_type_id"]
    if "slot_type_name" in value:
        out["slotTypeName"] = value["slot_type_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "slot_type_values" in value:
        import capo_lex_models_v2.types.slot_type_values

        out["slotTypeValues"] = (
            capo_lex_models_v2.types.slot_type_values.serialize_json(
                value["slot_type_values"]
            )
        )
    if "value_selection_setting" in value:
        import capo_lex_models_v2.types.slot_value_selection_setting

        out["valueSelectionSetting"] = (
            capo_lex_models_v2.types.slot_value_selection_setting.serialize_json(
                value["value_selection_setting"]
            )
        )
    if "parent_slot_type_signature" in value:
        out["parentSlotTypeSignature"] = value["parent_slot_type_signature"]
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    if "external_source_setting" in value:
        import capo_lex_models_v2.types.external_source_setting

        out["externalSourceSetting"] = (
            capo_lex_models_v2.types.external_source_setting.serialize_json(
                value["external_source_setting"]
            )
        )
    if "composite_slot_type_setting" in value:
        import capo_lex_models_v2.types.composite_slot_type_setting

        out["compositeSlotTypeSetting"] = (
            capo_lex_models_v2.types.composite_slot_type_setting.serialize_json(
                value["composite_slot_type_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSlotTypeResponse:
    out: UpdateSlotTypeResponse = {}  # type: ignore[typeddict-item]
    if "slotTypeId" in data:
        out["slot_type_id"] = data["slotTypeId"]
    if "slotTypeName" in data:
        out["slot_type_name"] = data["slotTypeName"]
    if "description" in data:
        out["description"] = data["description"]
    if "slotTypeValues" in data:
        import capo_lex_models_v2.types.slot_type_values

        out["slot_type_values"] = (
            capo_lex_models_v2.types.slot_type_values.deserialize_json(
                data["slotTypeValues"]
            )
        )
    if "valueSelectionSetting" in data:
        import capo_lex_models_v2.types.slot_value_selection_setting

        out["value_selection_setting"] = (
            capo_lex_models_v2.types.slot_value_selection_setting.deserialize_json(
                data["valueSelectionSetting"]
            )
        )
    if "parentSlotTypeSignature" in data:
        out["parent_slot_type_signature"] = data["parentSlotTypeSignature"]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "lastUpdatedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "externalSourceSetting" in data:
        import capo_lex_models_v2.types.external_source_setting

        out["external_source_setting"] = (
            capo_lex_models_v2.types.external_source_setting.deserialize_json(
                data["externalSourceSetting"]
            )
        )
    if "compositeSlotTypeSetting" in data:
        import capo_lex_models_v2.types.composite_slot_type_setting

        out["composite_slot_type_setting"] = (
            capo_lex_models_v2.types.composite_slot_type_setting.deserialize_json(
                data["compositeSlotTypeSetting"]
            )
        )
    return out
