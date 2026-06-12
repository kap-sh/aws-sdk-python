"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.choice_id
    import aws_sdk_wellarchitected.types.choice_update

ChoiceUpdates: TypeAlias = dict[
    "aws_sdk_wellarchitected.types.choice_id.ChoiceId",
    "aws_sdk_wellarchitected.types.choice_update.ChoiceUpdate",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ChoiceUpdates) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_wellarchitected.types.choice_update

        out[key] = aws_sdk_wellarchitected.types.choice_update.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ChoiceUpdates:
    out: ChoiceUpdates = {}
    for key, value in data.items():
        import aws_sdk_wellarchitected.types.choice_update

        out[key] = aws_sdk_wellarchitected.types.choice_update.deserialize_json(value)
    return out
