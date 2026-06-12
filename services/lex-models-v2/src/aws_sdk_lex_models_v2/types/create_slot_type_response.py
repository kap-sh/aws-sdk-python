"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateSlotTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.composite_slot_type_setting
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.external_source_setting
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.slot_type_signature
    import aws_sdk_lex_models_v2.types.slot_type_values
    import aws_sdk_lex_models_v2.types.slot_value_selection_setting
    import aws_sdk_lex_models_v2.types.timestamp


class CreateSlotTypeResponse(TypedDict):
    slot_type_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier assigned to the slot type. Use this to identify the slot type in the <code>UpdateSlotType</code> and <code>DeleteSlotType</code> operations.</p>"""
    slot_type_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name specified for the slot type.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description specified for the slot type.</p>"""
    slot_type_values: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_type_values.SlotTypeValues"
    ]
    """<p>The list of values that the slot type can assume.</p>"""
    value_selection_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_value_selection_setting.SlotValueSelectionSetting"
    ]
    """<p>The strategy that Amazon Lex uses to select a value from the list of possible values.</p>"""
    parent_slot_type_signature: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_type_signature.SlotTypeSignature"
    ]
    """<p>The signature of the base slot type specified for the slot type.</p>"""
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier for the bot associated with the slot type.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot associated with the slot type.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The specified language and local specified for the slot type.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the slot type was created.</p>"""
    external_source_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.external_source_setting.ExternalSourceSetting"
    ]
    """<p>The type of external information used to create the slot type.</p>"""
    composite_slot_type_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.composite_slot_type_setting.CompositeSlotTypeSetting"
    ]
    """<p>Specifications for a composite slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSlotTypeResponse) -> dict:
    out: dict = {}
    if "slot_type_id" in value:
        out["slotTypeId"] = value["slot_type_id"]
    if "slot_type_name" in value:
        out["slotTypeName"] = value["slot_type_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "slot_type_values" in value:
        import aws_sdk_lex_models_v2.types.slot_type_values

        out["slotTypeValues"] = (
            aws_sdk_lex_models_v2.types.slot_type_values.serialize_json(
                value["slot_type_values"]
            )
        )
    if "value_selection_setting" in value:
        import aws_sdk_lex_models_v2.types.slot_value_selection_setting

        out["valueSelectionSetting"] = (
            aws_sdk_lex_models_v2.types.slot_value_selection_setting.serialize_json(
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
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "external_source_setting" in value:
        import aws_sdk_lex_models_v2.types.external_source_setting

        out["externalSourceSetting"] = (
            aws_sdk_lex_models_v2.types.external_source_setting.serialize_json(
                value["external_source_setting"]
            )
        )
    if "composite_slot_type_setting" in value:
        import aws_sdk_lex_models_v2.types.composite_slot_type_setting

        out["compositeSlotTypeSetting"] = (
            aws_sdk_lex_models_v2.types.composite_slot_type_setting.serialize_json(
                value["composite_slot_type_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSlotTypeResponse:
    out: CreateSlotTypeResponse = {}  # type: ignore[typeddict-item]
    if "slotTypeId" in data:
        out["slot_type_id"] = data["slotTypeId"]
    if "slotTypeName" in data:
        out["slot_type_name"] = data["slotTypeName"]
    if "description" in data:
        out["description"] = data["description"]
    if "slotTypeValues" in data:
        import aws_sdk_lex_models_v2.types.slot_type_values

        out["slot_type_values"] = (
            aws_sdk_lex_models_v2.types.slot_type_values.deserialize_json(
                data["slotTypeValues"]
            )
        )
    if "valueSelectionSetting" in data:
        import aws_sdk_lex_models_v2.types.slot_value_selection_setting

        out["value_selection_setting"] = (
            aws_sdk_lex_models_v2.types.slot_value_selection_setting.deserialize_json(
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
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "externalSourceSetting" in data:
        import aws_sdk_lex_models_v2.types.external_source_setting

        out["external_source_setting"] = (
            aws_sdk_lex_models_v2.types.external_source_setting.deserialize_json(
                data["externalSourceSetting"]
            )
        )
    if "compositeSlotTypeSetting" in data:
        import aws_sdk_lex_models_v2.types.composite_slot_type_setting

        out["composite_slot_type_setting"] = (
            aws_sdk_lex_models_v2.types.composite_slot_type_setting.deserialize_json(
                data["compositeSlotTypeSetting"]
            )
        )
    return out
