"""Generated from Smithy shape ``com.amazonaws.amp#ScraperFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amp.types.filter_key
    import capo_amp.types.filter_values

ScraperFilters: TypeAlias = dict[
    "capo_amp.types.filter_key.FilterKey", "capo_amp.types.filter_values.FilterValues"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ScraperFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_amp.types.filter_values

        out[key] = capo_amp.types.filter_values.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ScraperFilters:
    out: ScraperFilters = {}
    for key, value in data.items():
        import capo_amp.types.filter_values

        out[key] = capo_amp.types.filter_values.deserialize_json(value)
    return out
