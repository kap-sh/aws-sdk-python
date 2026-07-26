"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#FilterRequirement``."""

from typing import Literal, TypeAlias, cast

"""<p> Enumeration of condition matching requirements: MEETS_ALL requires all conditions to match, MEETS_ANY requires at least one. </p>"""
FilterRequirement: TypeAlias = Literal[
    "MEETS_ALL",
    "MEETS_ANY",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterRequirement) -> str:
    return value


def deserialize_json(data: str) -> FilterRequirement:
    return cast(FilterRequirement, data)
