"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfListJobsFilterTerm``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.list_jobs_filter_term

__listOfListJobsFilterTerm: TypeAlias = list[
    "capo_macie2.types.list_jobs_filter_term.ListJobsFilterTerm"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfListJobsFilterTerm) -> list:
    import capo_macie2.types.list_jobs_filter_term

    out: list = []
    for item in value:
        out.append(capo_macie2.types.list_jobs_filter_term.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfListJobsFilterTerm:
    import capo_macie2.types.list_jobs_filter_term

    out: __listOfListJobsFilterTerm = []
    for item in data:
        out.append(capo_macie2.types.list_jobs_filter_term.deserialize_json(item))
    return out
