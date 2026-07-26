"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FilterCriteriaMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.criterion

FilterCriteriaMap: TypeAlias = dict[
    "str", "capo_accessanalyzer.types.criterion.Criterion"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FilterCriteriaMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_accessanalyzer.types.criterion

        out[key] = capo_accessanalyzer.types.criterion.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FilterCriteriaMap:
    out: FilterCriteriaMap = {}
    for key, value in data.items():
        import capo_accessanalyzer.types.criterion

        out[key] = capo_accessanalyzer.types.criterion.deserialize_json(value)
    return out
