"""Generated from Smithy shape ``com.amazonaws.macie2#Criterion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.criterion_additional_properties

Criterion: TypeAlias = dict[
    "capo_macie2.types.__string.__string",
    "capo_macie2.types.criterion_additional_properties.CriterionAdditionalProperties",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Criterion) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_macie2.types.criterion_additional_properties

        out[key] = capo_macie2.types.criterion_additional_properties.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> Criterion:
    out: Criterion = {}
    for key, value in data.items():
        import capo_macie2.types.criterion_additional_properties

        out[key] = capo_macie2.types.criterion_additional_properties.deserialize_json(
            value
        )
    return out
