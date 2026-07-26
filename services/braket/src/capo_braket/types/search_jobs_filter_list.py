"""Generated from Smithy shape ``com.amazonaws.braket#SearchJobsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.search_jobs_filter

SearchJobsFilterList: TypeAlias = list[
    "capo_braket.types.search_jobs_filter.SearchJobsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobsFilterList) -> list:
    import capo_braket.types.search_jobs_filter

    out: list = []
    for item in value:
        out.append(capo_braket.types.search_jobs_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchJobsFilterList:
    import capo_braket.types.search_jobs_filter

    out: SearchJobsFilterList = []
    for item in data:
        out.append(capo_braket.types.search_jobs_filter.deserialize_json(item))
    return out
