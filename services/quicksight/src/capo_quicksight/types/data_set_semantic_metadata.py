"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetSemanticMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.custom_instruction_list
    import capo_quicksight.types.data_set_semantic_description


class DataSetSemanticMetadata(TypedDict, closed=True):
    description: NotRequired[
        "capo_quicksight.types.data_set_semantic_description.DataSetSemanticDescription"
    ]
    """<p>A description of the dataset.</p>"""
    custom_instructions: NotRequired[
        "capo_quicksight.types.custom_instruction_list.CustomInstructionList"
    ]
    """<p>A list of custom instructions that guide how the dataset should be consumed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSemanticMetadata) -> dict:
    out: dict = {}
    if "description" in value:
        import capo_quicksight.types.data_set_semantic_description

        out["Description"] = (
            capo_quicksight.types.data_set_semantic_description.serialize_json(
                value["description"]
            )
        )
    if "custom_instructions" in value:
        import capo_quicksight.types.custom_instruction_list

        out["CustomInstructions"] = (
            capo_quicksight.types.custom_instruction_list.serialize_json(
                value["custom_instructions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetSemanticMetadata:
    out: DataSetSemanticMetadata = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        import capo_quicksight.types.data_set_semantic_description

        out["description"] = (
            capo_quicksight.types.data_set_semantic_description.deserialize_json(
                data["Description"]
            )
        )
    if "CustomInstructions" in data:
        import capo_quicksight.types.custom_instruction_list

        out["custom_instructions"] = (
            capo_quicksight.types.custom_instruction_list.deserialize_json(
                data["CustomInstructions"]
            )
        )
    return out
