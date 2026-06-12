"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeSlotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.built_in_or_custom_slot_type_id
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.multiple_values_setting
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.obfuscation_setting
    import aws_sdk_lex_models_v2.types.slot_value_elicitation_setting
    import aws_sdk_lex_models_v2.types.sub_slot_setting
    import aws_sdk_lex_models_v2.types.timestamp


class DescribeSlotResponse(TypedDict):
    slot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier generated for the slot.</p>"""
    slot_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name specified for the slot.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description specified for the slot.</p>"""
    slot_type_id: NotRequired[
        "aws_sdk_lex_models_v2.types.built_in_or_custom_slot_type_id.BuiltInOrCustomSlotTypeId"
    ]
    """<p>The identifier of the slot type that determines the values entered into the slot.</p>"""
    value_elicitation_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_value_elicitation_setting.SlotValueElicitationSetting"
    ]
    """<p>Prompts that Amazon Lex uses to elicit a value for the slot.</p>"""
    obfuscation_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.obfuscation_setting.ObfuscationSetting"
    ]
    """<p>Whether slot values are shown in Amazon CloudWatch logs. If the value is <code>None</code>, the actual value of the slot is shown in logs.</p>"""
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot associated with the slot.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot associated with the slot.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The language and locale specified for the slot.</p>"""
    intent_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the intent associated with the slot.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the slot was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of the date and time that the slot was last updated.</p>"""
    multiple_values_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.multiple_values_setting.MultipleValuesSetting"
    ]
    """<p>Indicates whether the slot accepts multiple values in a single utterance.</p> <p>If the <code>multipleValuesSetting</code> is not set, the default value is <code>false</code>.</p>"""
    sub_slot_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.sub_slot_setting.SubSlotSetting"
    ]
    """<p>Specifications for the constituent sub slots and the expression for the composite slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSlotResponse) -> dict:
    out: dict = {}
    if "slot_id" in value:
        out["slotId"] = value["slot_id"]
    if "slot_name" in value:
        out["slotName"] = value["slot_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "slot_type_id" in value:
        out["slotTypeId"] = value["slot_type_id"]
    if "value_elicitation_setting" in value:
        import aws_sdk_lex_models_v2.types.slot_value_elicitation_setting

        out["valueElicitationSetting"] = (
            aws_sdk_lex_models_v2.types.slot_value_elicitation_setting.serialize_json(
                value["value_elicitation_setting"]
            )
        )
    if "obfuscation_setting" in value:
        import aws_sdk_lex_models_v2.types.obfuscation_setting

        out["obfuscationSetting"] = (
            aws_sdk_lex_models_v2.types.obfuscation_setting.serialize_json(
                value["obfuscation_setting"]
            )
        )
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "intent_id" in value:
        out["intentId"] = value["intent_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    if "multiple_values_setting" in value:
        import aws_sdk_lex_models_v2.types.multiple_values_setting

        out["multipleValuesSetting"] = (
            aws_sdk_lex_models_v2.types.multiple_values_setting.serialize_json(
                value["multiple_values_setting"]
            )
        )
    if "sub_slot_setting" in value:
        import aws_sdk_lex_models_v2.types.sub_slot_setting

        out["subSlotSetting"] = (
            aws_sdk_lex_models_v2.types.sub_slot_setting.serialize_json(
                value["sub_slot_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeSlotResponse:
    out: DescribeSlotResponse = {}  # type: ignore[typeddict-item]
    if "slotId" in data:
        out["slot_id"] = data["slotId"]
    if "slotName" in data:
        out["slot_name"] = data["slotName"]
    if "description" in data:
        out["description"] = data["description"]
    if "slotTypeId" in data:
        out["slot_type_id"] = data["slotTypeId"]
    if "valueElicitationSetting" in data:
        import aws_sdk_lex_models_v2.types.slot_value_elicitation_setting

        out["value_elicitation_setting"] = (
            aws_sdk_lex_models_v2.types.slot_value_elicitation_setting.deserialize_json(
                data["valueElicitationSetting"]
            )
        )
    if "obfuscationSetting" in data:
        import aws_sdk_lex_models_v2.types.obfuscation_setting

        out["obfuscation_setting"] = (
            aws_sdk_lex_models_v2.types.obfuscation_setting.deserialize_json(
                data["obfuscationSetting"]
            )
        )
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "intentId" in data:
        out["intent_id"] = data["intentId"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "multipleValuesSetting" in data:
        import aws_sdk_lex_models_v2.types.multiple_values_setting

        out["multiple_values_setting"] = (
            aws_sdk_lex_models_v2.types.multiple_values_setting.deserialize_json(
                data["multipleValuesSetting"]
            )
        )
    if "subSlotSetting" in data:
        import aws_sdk_lex_models_v2.types.sub_slot_setting

        out["sub_slot_setting"] = (
            aws_sdk_lex_models_v2.types.sub_slot_setting.deserialize_json(
                data["subSlotSetting"]
            )
        )
    return out
