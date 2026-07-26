"""Generated from Smithy shape ``com.amazonaws.macie2#BucketCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.bucket_criteria_additional_properties

BucketCriteria: TypeAlias = dict[
    "capo_macie2.types.__string.__string",
    "capo_macie2.types.bucket_criteria_additional_properties.BucketCriteriaAdditionalProperties",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: BucketCriteria) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_macie2.types.bucket_criteria_additional_properties

        out[key] = (
            capo_macie2.types.bucket_criteria_additional_properties.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> BucketCriteria:
    out: BucketCriteria = {}
    for key, value in data.items():
        import capo_macie2.types.bucket_criteria_additional_properties

        out[key] = (
            capo_macie2.types.bucket_criteria_additional_properties.deserialize_json(
                value
            )
        )
    return out
