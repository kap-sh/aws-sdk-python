"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SubSlotSpecificationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.specifications

SubSlotSpecificationMap: TypeAlias = dict[
    "capo_lex_models_v2.types.name.Name",
    "capo_lex_models_v2.types.specifications.Specifications",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SubSlotSpecificationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_models_v2.types.specifications

        out[key] = capo_lex_models_v2.types.specifications.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SubSlotSpecificationMap:
    out: SubSlotSpecificationMap = {}
    for key, value in data.items():
        import capo_lex_models_v2.types.specifications

        out[key] = capo_lex_models_v2.types.specifications.deserialize_json(value)
    return out
