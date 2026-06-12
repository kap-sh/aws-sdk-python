"""Generated from Smithy shape ``com.amazonaws.wellarchitected#SelectedChoiceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.choice_id

SelectedChoiceIds: TypeAlias = list["aws_sdk_wellarchitected.types.choice_id.ChoiceId"]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedChoiceIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SelectedChoiceIds:
    return list(data)
