"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.slot_type_category
    import aws_sdk_lex_models_v2.types.slot_type_signature
    import aws_sdk_lex_models_v2.types.timestamp


class SlotTypeSummary(TypedDict):
    slot_type_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier assigned to the slot type.</p>"""
    slot_type_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of the slot type.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description of the slot type.</p>"""
    parent_slot_type_signature: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_type_signature.SlotTypeSignature"
    ]
    """<p>If the slot type is derived from a built-on slot type, the name of the parent slot type.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of the date and time that the slot type was last updated.</p>"""
    slot_type_category: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_type_category.SlotTypeCategory"
    ]
    """<p>Indicates the type of the slot type.</p> <ul> <li> <p> <code>Custom</code> - A slot type that you created using custom values. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/custom-slot-types.html\">Creating custom slot types</a>.</p> </li> <li> <p> <code>Extended</code> - A slot type created by extending the <code>AMAZON.AlphaNumeric</code> built-in slot type. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-alphanumerice.html\"> <code>AMAZON.AlphaNumeric</code> </a>.</p> </li> <li> <p> <code>ExternalGrammar</code> - A slot type using a custom GRXML grammar to define values. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/building-grxml.html\">Using a custom grammar slot type</a>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeSummary) -> dict:
    out: dict = {}
    if "slot_type_id" in value:
        out["slotTypeId"] = value["slot_type_id"]
    if "slot_type_name" in value:
        out["slotTypeName"] = value["slot_type_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parent_slot_type_signature" in value:
        out["parentSlotTypeSignature"] = value["parent_slot_type_signature"]
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    if "slot_type_category" in value:
        import aws_sdk_lex_models_v2.types.slot_type_category

        out["slotTypeCategory"] = (
            aws_sdk_lex_models_v2.types.slot_type_category.serialize_json(
                value["slot_type_category"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlotTypeSummary:
    out: SlotTypeSummary = {}  # type: ignore[typeddict-item]
    if "slotTypeId" in data:
        out["slot_type_id"] = data["slotTypeId"]
    if "slotTypeName" in data:
        out["slot_type_name"] = data["slotTypeName"]
    if "description" in data:
        out["description"] = data["description"]
    if "parentSlotTypeSignature" in data:
        out["parent_slot_type_signature"] = data["parentSlotTypeSignature"]
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "slotTypeCategory" in data:
        import aws_sdk_lex_models_v2.types.slot_type_category

        out["slot_type_category"] = (
            aws_sdk_lex_models_v2.types.slot_type_category.deserialize_json(
                data["slotTypeCategory"]
            )
        )
    return out
