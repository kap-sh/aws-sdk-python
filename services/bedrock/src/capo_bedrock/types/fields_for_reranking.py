"""Generated from Smithy shape ``com.amazonaws.bedrock#FieldsForReranking``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.field_for_reranking

FieldsForReranking: TypeAlias = list[
    "capo_bedrock.types.field_for_reranking.FieldForReranking"
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldsForReranking) -> list:
    import capo_bedrock.types.field_for_reranking

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.field_for_reranking.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldsForReranking:
    import capo_bedrock.types.field_for_reranking

    out: FieldsForReranking = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.field_for_reranking.deserialize_json(item))
    return out
