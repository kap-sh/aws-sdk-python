"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Stats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.field_stats
    import capo_cloudsearch_domain.types.string

Stats: TypeAlias = dict[
    "capo_cloudsearch_domain.types.string.String",
    "capo_cloudsearch_domain.types.field_stats.FieldStats",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Stats) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_cloudsearch_domain.types.field_stats

        out[key] = capo_cloudsearch_domain.types.field_stats.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Stats:
    out: Stats = {}
    for key, value in data.items():
        import capo_cloudsearch_domain.types.field_stats

        out[key] = capo_cloudsearch_domain.types.field_stats.deserialize_json(value)
    return out
