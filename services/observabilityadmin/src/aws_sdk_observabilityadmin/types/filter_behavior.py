"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#FilterBehavior``."""

from typing import Literal, TypeAlias, cast

"""<p> Enumeration of filter actions: KEEP to include log records, DROP to exclude them. </p>"""
FilterBehavior: TypeAlias = Literal[
    "KEEP",
    "DROP",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterBehavior) -> str:
    return value


def deserialize_json(data: str) -> FilterBehavior:
    return cast(FilterBehavior, data)
