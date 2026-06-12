"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationNotesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_note
    import aws_sdk_connect.types.resource_id

EvaluationNotesMap: TypeAlias = dict[
    "aws_sdk_connect.types.resource_id.ResourceId",
    "aws_sdk_connect.types.evaluation_note.EvaluationNote",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EvaluationNotesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_connect.types.evaluation_note

        out[key] = aws_sdk_connect.types.evaluation_note.serialize_json(value)
    return out


def deserialize_json(data: dict) -> EvaluationNotesMap:
    out: EvaluationNotesMap = {}
    for key, value in data.items():
        import aws_sdk_connect.types.evaluation_note

        out[key] = aws_sdk_connect.types.evaluation_note.deserialize_json(value)
    return out
