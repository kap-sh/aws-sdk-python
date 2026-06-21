"""Generated from Smithy shape ``com.amazonaws.macie2#JobComparator``."""

from typing import Literal, TypeAlias, cast

"""<p>The operator to use in a condition. Depending on the type of condition, possible values are:</p>"""
JobComparator: TypeAlias = Literal[
    "EQ",
    "GT",
    "GTE",
    "LT",
    "LTE",
    "NE",
    "CONTAINS",
    "STARTS_WITH",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobComparator) -> str:
    return value


def deserialize_json(data: str) -> JobComparator:
    return cast(JobComparator, data)
