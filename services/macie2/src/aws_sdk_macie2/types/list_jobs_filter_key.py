"""Generated from Smithy shape ``com.amazonaws.macie2#ListJobsFilterKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The property to use to filter the results. Valid values are:</p>"""
ListJobsFilterKey: TypeAlias = Literal[
    "jobType",
    "jobStatus",
    "createdAt",
    "name",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ListJobsFilterKey:
    return cast(ListJobsFilterKey, data)
