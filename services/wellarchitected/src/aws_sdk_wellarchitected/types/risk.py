"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Risk``."""

from typing import Literal, TypeAlias, cast

"""<p>The risk for a given workload, lens review, pillar, or question.</p>"""
Risk: TypeAlias = Literal[
    "UNANSWERED",
    "HIGH",
    "MEDIUM",
    "NONE",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Risk) -> str:
    return value


def deserialize_json(data: str) -> Risk:
    return cast(Risk, data)
