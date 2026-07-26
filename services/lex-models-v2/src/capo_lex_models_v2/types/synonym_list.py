"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SynonymList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.sample_value

SynonymList: TypeAlias = list["capo_lex_models_v2.types.sample_value.SampleValue"]


# --- restJson1 ser/de ---
def serialize_json(value: SynonymList) -> list:
    import capo_lex_models_v2.types.sample_value

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.sample_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> SynonymList:
    import capo_lex_models_v2.types.sample_value

    out: SynonymList = []
    for item in data:
        out.append(capo_lex_models_v2.types.sample_value.deserialize_json(item))
    return out
