"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateSlotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.built_in_or_custom_slot_type_id
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.multiple_values_setting
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.obfuscation_setting
    import aws_sdk_lex_models_v2.types.slot_value_elicitation_setting
    import aws_sdk_lex_models_v2.types.sub_slot_setting


class CreateSlotRequest(TypedDict, closed=True):
    slot_name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the slot. Slot names must be unique within the bot that contains the slot.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>A description of the slot. Use this to help identify the slot in lists.</p>"""
    slot_type_id: NotRequired[
        "aws_sdk_lex_models_v2.types.built_in_or_custom_slot_type_id.BuiltInOrCustomSlotTypeId"
    ]
    """<p>The unique identifier for the slot type associated with this slot. The slot type determines the values that can be entered into the slot.</p>"""
    value_elicitation_setting: "aws_sdk_lex_models_v2.types.slot_value_elicitation_setting.SlotValueElicitationSetting"
    """<p>Specifies prompts that Amazon Lex sends to the user to elicit a response that provides the value for the slot. </p>"""
    obfuscation_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.obfuscation_setting.ObfuscationSetting"
    ]
    """<p>Determines how slot values are used in Amazon CloudWatch logs. If the value of the <code>obfuscationSetting</code> parameter is <code>DefaultObfuscation</code>, slot values are obfuscated in the log output. If the value is <code>None</code>, the actual value is present in the log output.</p> <p>The default is to obfuscate values in the CloudWatch logs.</p>"""
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with the slot.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot associated with the slot.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    r"""<p>The identifier of the language and locale that the slot will be used in. The string must match one of the supported locales. All of the bots, intents, slot types used by the slot must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""
    intent_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the intent that contains the slot.</p>"""
    multiple_values_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.multiple_values_setting.MultipleValuesSetting"
    ]
    """<p>Indicates whether the slot returns multiple values in one response. Multi-value slots are only available in the <code>en-US</code> locale. If you set this value to <code>true</code> in any other locale, Amazon Lex throws a <code>ValidationException</code>. </p> <p>If the <code>multipleValuesSetting</code> is not set, the default value is <code>false</code>.</p>"""
    sub_slot_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.sub_slot_setting.SubSlotSetting"
    ]
    """<p>Specifications for the constituent sub slots and the expression for the composite slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSlotRequest) -> dict:
    out: dict = {}
    out["slotName"] = value["slot_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "slot_type_id" in value:
        out["slotTypeId"] = value["slot_type_id"]
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


def deserialize_json(data: dict) -> CreateSlotRequest:
    out: CreateSlotRequest = {}  # type: ignore[typeddict-item]
    if "slotName" in data:
        out["slot_name"] = data["slotName"]
    else:
        raise DeserializationError("CreateSlotRequest.slot_name required")
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
    else:
        raise DeserializationError(
            "CreateSlotRequest.value_elicitation_setting required"
        )
    if "obfuscationSetting" in data:
        import aws_sdk_lex_models_v2.types.obfuscation_setting

        out["obfuscation_setting"] = (
            aws_sdk_lex_models_v2.types.obfuscation_setting.deserialize_json(
                data["obfuscationSetting"]
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
