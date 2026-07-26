"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_weight
    import capo_connect.types.evaluation_form_items_list
    import capo_connect.types.evaluation_form_question_instructions
    import capo_connect.types.evaluation_form_section_title
    import capo_connect.types.reference_id


class EvaluationFormSection(TypedDict, closed=True):
    title: "capo_connect.types.evaluation_form_section_title.EvaluationFormSectionTitle"
    """<p>The title of the section.</p>"""
    ref_id: "capo_connect.types.reference_id.ReferenceId"
    """<p>The identifier of the section. An identifier must be unique within the evaluation form.</p>"""
    instructions: NotRequired[
        "capo_connect.types.evaluation_form_question_instructions.EvaluationFormQuestionInstructions"
    ]
    """<p>The instructions of the section.</p>"""
    items: "capo_connect.types.evaluation_form_items_list.EvaluationFormItemsList"
    """<p>The items of the section.</p>"""
    weight: "capo_connect.types.evaluation_form_item_weight.EvaluationFormItemWeight"
    """<p>The scoring weight of the section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSection) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    out["RefId"] = value["ref_id"]
    if "instructions" in value:
        out["Instructions"] = value["instructions"]
    import capo_connect.types.evaluation_form_items_list

    out["Items"] = capo_connect.types.evaluation_form_items_list.serialize_json(
        value["items"]
    )
    out["Weight"] = value.get("weight", 0)
    return out


def deserialize_json(data: dict) -> EvaluationFormSection:
    out: EvaluationFormSection = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("EvaluationFormSection.title required")
    if "RefId" in data:
        out["ref_id"] = data["RefId"]
    else:
        raise DeserializationError("EvaluationFormSection.ref_id required")
    if "Instructions" in data:
        out["instructions"] = data["Instructions"]
    if "Items" in data:
        import capo_connect.types.evaluation_form_items_list

        out["items"] = capo_connect.types.evaluation_form_items_list.deserialize_json(
            data["Items"]
        )
    else:
        raise DeserializationError("EvaluationFormSection.items required")
    if "Weight" in data:
        out["weight"] = data["Weight"]
    else:
        out["weight"] = 0
    return out
