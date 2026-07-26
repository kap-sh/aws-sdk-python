"""Generated from Smithy shape ``com.amazonaws.macie2#ListJobsSortAttributeName``."""

from typing import Literal, TypeAlias, cast

"""<p>The property to sort the results by. Valid values are:</p>"""
ListJobsSortAttributeName: TypeAlias = Literal[
    "createdAt",
    "jobStatus",
    "name",
    "jobType",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsSortAttributeName) -> str:
    return value


def deserialize_json(data: str) -> ListJobsSortAttributeName:
    return cast(ListJobsSortAttributeName, data)
