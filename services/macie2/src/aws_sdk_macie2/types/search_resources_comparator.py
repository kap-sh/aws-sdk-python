"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesComparator``."""

from typing import Literal, TypeAlias, cast

"""<p>The operator to use in a condition that filters the results of a query. Valid values are:</p>"""
SearchResourcesComparator: TypeAlias = Literal[
    "EQ",
    "NE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesComparator) -> str:
    return value


def deserialize_json(data: str) -> SearchResourcesComparator:
    return cast(SearchResourcesComparator, data)
