"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.built_in_or_custom_slot_type_id
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.prompt_specification
    import aws_sdk_lex_models_v2.types.slot_constraint
    import aws_sdk_lex_models_v2.types.timestamp


class SlotSummary(TypedDict):
    slot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the slot.</p>"""
    slot_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name given to the slot.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description of the slot.</p>"""
    slot_constraint: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_constraint.SlotConstraint"
    ]
    """<p>Whether the slot is required or optional. An intent is complete when all required slots are filled.</p>"""
    slot_type_id: NotRequired[
        "aws_sdk_lex_models_v2.types.built_in_or_custom_slot_type_id.BuiltInOrCustomSlotTypeId"
    ]
    """<p>The unique identifier for the slot type that defines the values for the slot.</p>"""
    value_elicitation_prompt_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.prompt_specification.PromptSpecification"
    ]
    """<p>Prompts that are sent to the user to elicit a value for the slot.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the last date and time that the slot was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotSummary) -> dict:
    out: dict = {}
    if "slot_id" in value:
        out["slotId"] = value["slot_id"]
    if "slot_name" in value:
        out["slotName"] = value["slot_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "slot_constraint" in value:
        import aws_sdk_lex_models_v2.types.slot_constraint

        out["slotConstraint"] = (
            aws_sdk_lex_models_v2.types.slot_constraint.serialize_json(
                value["slot_constraint"]
            )
        )
    if "slot_type_id" in value:
        out["slotTypeId"] = value["slot_type_id"]
    if "value_elicitation_prompt_specification" in value:
        import aws_sdk_lex_models_v2.types.prompt_specification

        out["valueElicitationPromptSpecification"] = (
            aws_sdk_lex_models_v2.types.prompt_specification.serialize_json(
                value["value_elicitation_prompt_specification"]
            )
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlotSummary:
    out: SlotSummary = {}  # type: ignore[typeddict-item]
    if "slotId" in data:
        out["slot_id"] = data["slotId"]
    if "slotName" in data:
        out["slot_name"] = data["slotName"]
    if "description" in data:
        out["description"] = data["description"]
    if "slotConstraint" in data:
        import aws_sdk_lex_models_v2.types.slot_constraint

        out["slot_constraint"] = (
            aws_sdk_lex_models_v2.types.slot_constraint.deserialize_json(
                data["slotConstraint"]
            )
        )
    if "slotTypeId" in data:
        out["slot_type_id"] = data["slotTypeId"]
    if "valueElicitationPromptSpecification" in data:
        import aws_sdk_lex_models_v2.types.prompt_specification

        out["value_elicitation_prompt_specification"] = (
            aws_sdk_lex_models_v2.types.prompt_specification.deserialize_json(
                data["valueElicitationPromptSpecification"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out
