"""Generated from Smithy shape ``com.amazonaws.rtbfabric#FilterCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.filter_criterion

FilterCriteria: TypeAlias = list[
    "capo_rtbfabric.types.filter_criterion.FilterCriterion"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteria) -> list:
    import capo_rtbfabric.types.filter_criterion

    out: list = []
    for item in value:
        out.append(capo_rtbfabric.types.filter_criterion.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterCriteria:
    import capo_rtbfabric.types.filter_criterion

    out: FilterCriteria = []
    for item in data:
        out.append(capo_rtbfabric.types.filter_criterion.deserialize_json(item))
    return out
