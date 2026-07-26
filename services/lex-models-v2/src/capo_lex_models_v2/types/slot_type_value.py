"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.sample_value
    import capo_lex_models_v2.types.synonym_list


class SlotTypeValue(TypedDict, closed=True):
    sample_value: NotRequired["capo_lex_models_v2.types.sample_value.SampleValue"]
    """<p>The value of the slot type entry.</p>"""
    synonyms: NotRequired["capo_lex_models_v2.types.synonym_list.SynonymList"]
    """<p>Additional values related to the slot type entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeValue) -> dict:
    out: dict = {}
    if "sample_value" in value:
        import capo_lex_models_v2.types.sample_value

        out["sampleValue"] = capo_lex_models_v2.types.sample_value.serialize_json(
            value["sample_value"]
        )
    if "synonyms" in value:
        import capo_lex_models_v2.types.synonym_list

        out["synonyms"] = capo_lex_models_v2.types.synonym_list.serialize_json(
            value["synonyms"]
        )
    return out


def deserialize_json(data: dict) -> SlotTypeValue:
    out: SlotTypeValue = {}  # type: ignore[typeddict-item]
    if "sampleValue" in data:
        import capo_lex_models_v2.types.sample_value

        out["sample_value"] = capo_lex_models_v2.types.sample_value.deserialize_json(
            data["sampleValue"]
        )
    if "synonyms" in data:
        import capo_lex_models_v2.types.synonym_list

        out["synonyms"] = capo_lex_models_v2.types.synonym_list.deserialize_json(
            data["synonyms"]
        )
    return out
