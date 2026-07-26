"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfAvailMatchingCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.avail_matching_criteria

__listOfAvailMatchingCriteria: TypeAlias = list[
    "capo_mediatailor.types.avail_matching_criteria.AvailMatchingCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAvailMatchingCriteria) -> list:
    import capo_mediatailor.types.avail_matching_criteria

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.avail_matching_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAvailMatchingCriteria:
    import capo_mediatailor.types.avail_matching_criteria

    out: __listOfAvailMatchingCriteria = []
    for item in data:
        out.append(
            capo_mediatailor.types.avail_matching_criteria.deserialize_json(item)
        )
    return out
