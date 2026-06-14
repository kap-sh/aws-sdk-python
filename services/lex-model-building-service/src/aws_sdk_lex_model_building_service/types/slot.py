"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Slot``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.custom_or_builtin_slot_type_name
    import aws_sdk_lex_model_building_service.types.description
    import aws_sdk_lex_model_building_service.types.obfuscation_setting
    import aws_sdk_lex_model_building_service.types.priority
    import aws_sdk_lex_model_building_service.types.prompt
    import aws_sdk_lex_model_building_service.types.response_card
    import aws_sdk_lex_model_building_service.types.slot_constraint
    import aws_sdk_lex_model_building_service.types.slot_default_value_spec
    import aws_sdk_lex_model_building_service.types.slot_name
    import aws_sdk_lex_model_building_service.types.slot_utterance_list
    import aws_sdk_lex_model_building_service.types.version


class Slot(TypedDict):
    name: "aws_sdk_lex_model_building_service.types.slot_name.SlotName"
    """<p>The name of the slot.</p>"""
    description: NotRequired[
        "aws_sdk_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the slot.</p>"""
    slot_constraint: (
        "aws_sdk_lex_model_building_service.types.slot_constraint.SlotConstraint"
    )
    """<p>Specifies whether the slot is required or optional. </p>"""
    slot_type: NotRequired[
        "aws_sdk_lex_model_building_service.types.custom_or_builtin_slot_type_name.CustomOrBuiltinSlotTypeName"
    ]
    """<p>The type of the slot, either a custom slot type that you defined or one of the built-in slot types.</p>"""
    slot_type_version: NotRequired[
        "aws_sdk_lex_model_building_service.types.version.Version"
    ]
    """<p>The version of the slot type.</p>"""
    value_elicitation_prompt: NotRequired[
        "aws_sdk_lex_model_building_service.types.prompt.Prompt"
    ]
    """<p>The prompt that Amazon Lex uses to elicit the slot value from the user.</p>"""
    priority: NotRequired["aws_sdk_lex_model_building_service.types.priority.Priority"]
    """<p> Directs Amazon Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Amazon Lex first elicits a value for the slot with priority 1.</p> <p>If multiple slots share the same priority, the order in which Amazon Lex elicits values is arbitrary.</p>"""
    sample_utterances: NotRequired[
        "aws_sdk_lex_model_building_service.types.slot_utterance_list.SlotUtteranceList"
    ]
    """<p> If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances. </p>"""
    response_card: NotRequired[
        "aws_sdk_lex_model_building_service.types.response_card.ResponseCard"
    ]
    """<p> A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply. </p>"""
    obfuscation_setting: NotRequired[
        "aws_sdk_lex_model_building_service.types.obfuscation_setting.ObfuscationSetting"
    ]
    r"""<p>Determines whether a slot is obfuscated in conversation logs and stored utterances. When you obfuscate a slot, the value is replaced by the slot name in curly braces ({}). For example, if the slot name is \"full_name\", obfuscated values are replaced with \"{full_name}\". For more information, see <a href=\"https://docs.aws.amazon.com/lex/latest/dg/how-obfuscate.html\"> Slot Obfuscation </a>. </p>"""
    default_value_spec: NotRequired[
        "aws_sdk_lex_model_building_service.types.slot_default_value_spec.SlotDefaultValueSpec"
    ]
    """<p>A list of default values for the slot. Default values are used when Amazon Lex hasn't determined a value for a slot. You can specify default values from context variables, session attributes, and defined values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Slot) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_lex_model_building_service.types.slot_constraint

    out["slotConstraint"] = (
        aws_sdk_lex_model_building_service.types.slot_constraint.serialize_json(
            value["slot_constraint"]
        )
    )
    if "slot_type" in value:
        out["slotType"] = value["slot_type"]
    if "slot_type_version" in value:
        out["slotTypeVersion"] = value["slot_type_version"]
    if "value_elicitation_prompt" in value:
        import aws_sdk_lex_model_building_service.types.prompt

        out["valueElicitationPrompt"] = (
            aws_sdk_lex_model_building_service.types.prompt.serialize_json(
                value["value_elicitation_prompt"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "sample_utterances" in value:
        import aws_sdk_lex_model_building_service.types.slot_utterance_list

        out["sampleUtterances"] = (
            aws_sdk_lex_model_building_service.types.slot_utterance_list.serialize_json(
                value["sample_utterances"]
            )
        )
    if "response_card" in value:
        out["responseCard"] = value["response_card"]
    if "obfuscation_setting" in value:
        import aws_sdk_lex_model_building_service.types.obfuscation_setting

        out["obfuscationSetting"] = (
            aws_sdk_lex_model_building_service.types.obfuscation_setting.serialize_json(
                value["obfuscation_setting"]
            )
        )
    if "default_value_spec" in value:
        import aws_sdk_lex_model_building_service.types.slot_default_value_spec

        out["defaultValueSpec"] = (
            aws_sdk_lex_model_building_service.types.slot_default_value_spec.serialize_json(
                value["default_value_spec"]
            )
        )
    return out


def deserialize_json(data: dict) -> Slot:
    out: Slot = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Slot.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "slotConstraint" in data:
        import aws_sdk_lex_model_building_service.types.slot_constraint

        out["slot_constraint"] = (
            aws_sdk_lex_model_building_service.types.slot_constraint.deserialize_json(
                data["slotConstraint"]
            )
        )
    else:
        raise DeserializationError("Slot.slot_constraint required")
    if "slotType" in data:
        out["slot_type"] = data["slotType"]
    if "slotTypeVersion" in data:
        out["slot_type_version"] = data["slotTypeVersion"]
    if "valueElicitationPrompt" in data:
        import aws_sdk_lex_model_building_service.types.prompt

        out["value_elicitation_prompt"] = (
            aws_sdk_lex_model_building_service.types.prompt.deserialize_json(
                data["valueElicitationPrompt"]
            )
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    if "sampleUtterances" in data:
        import aws_sdk_lex_model_building_service.types.slot_utterance_list

        out["sample_utterances"] = (
            aws_sdk_lex_model_building_service.types.slot_utterance_list.deserialize_json(
                data["sampleUtterances"]
            )
        )
    if "responseCard" in data:
        out["response_card"] = data["responseCard"]
    if "obfuscationSetting" in data:
        import aws_sdk_lex_model_building_service.types.obfuscation_setting

        out["obfuscation_setting"] = (
            aws_sdk_lex_model_building_service.types.obfuscation_setting.deserialize_json(
                data["obfuscationSetting"]
            )
        )
    if "defaultValueSpec" in data:
        import aws_sdk_lex_model_building_service.types.slot_default_value_spec

        out["default_value_spec"] = (
            aws_sdk_lex_model_building_service.types.slot_default_value_spec.deserialize_json(
                data["defaultValueSpec"]
            )
        )
    return out
