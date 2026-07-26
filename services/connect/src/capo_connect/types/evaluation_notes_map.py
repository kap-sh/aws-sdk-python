"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationNotesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_note
    import capo_connect.types.resource_id

EvaluationNotesMap: TypeAlias = dict[
    "capo_connect.types.resource_id.ResourceId",
    "capo_connect.types.evaluation_note.EvaluationNote",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EvaluationNotesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connect.types.evaluation_note

        out[key] = capo_connect.types.evaluation_note.serialize_json(value)
    return out


def deserialize_json(data: dict) -> EvaluationNotesMap:
    out: EvaluationNotesMap = {}
    for key, value in data.items():
        import capo_connect.types.evaluation_note

        out[key] = capo_connect.types.evaluation_note.deserialize_json(value)
    return out
