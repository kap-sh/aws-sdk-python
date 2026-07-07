"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateSlotTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

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


class CreateSlotTypeRequest(TypedDict, closed=True):
    slot_type_name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name for the slot. A slot type name must be unique within the intent.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>A description of the slot type. Use the description to help identify the slot type in lists.</p>"""
    slot_type_values: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_type_values.SlotTypeValues"
    ]
    """<p>A list of <code>SlotTypeValue</code> objects that defines the values that the slot type can take. Each value can have a list of synonyms, additional values that help train the machine learning model about the values that it resolves for a slot.</p>"""
    value_selection_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_value_selection_setting.SlotValueSelectionSetting"
    ]
    """<p>Determines the strategy that Amazon Lex uses to select a value from the list of possible values. The field can be set to one of the following values:</p> <ul> <li> <p> <code>ORIGINAL_VALUE</code> - Returns the value entered by the user, if the user value is similar to the slot value.</p> </li> <li> <p> <code>TOP_RESOLUTION</code> - If there is a resolution list for the slot, return the first value in the resolution list. If there is no resolution list, return null.</p> </li> </ul> <p>If you don't specify the <code>valueSelectionSetting</code> parameter, the default is <code>ORIGINAL_VALUE</code>.</p>"""
    parent_slot_type_signature: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_type_signature.SlotTypeSignature"
    ]
    """<p>The built-in slot type used as a parent of this slot type. When you define a parent slot type, the new slot type has the configuration of the parent slot type.</p> <p>Only <code>AMAZON.AlphaNumeric</code> is supported.</p>"""
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with this slot type.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The identifier of the bot version associated with this slot type.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    r"""<p>The identifier of the language and locale that the slot type will be used in. The string must match one of the supported locales. All of the bots, intents, and slots used by the slot type must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""
    external_source_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.external_source_setting.ExternalSourceSetting"
    ]
    """<p>Sets the type of external information used to create the slot type.</p>"""
    composite_slot_type_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.composite_slot_type_setting.CompositeSlotTypeSetting"
    ]
    """<p>Specifications for a composite slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSlotTypeRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> CreateSlotTypeRequest:
    out: CreateSlotTypeRequest = {}  # type: ignore[typeddict-item]
    if "slotTypeName" in data:
        out["slot_type_name"] = data["slotTypeName"]
    else:
        raise DeserializationError("CreateSlotTypeRequest.slot_type_name required")
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
