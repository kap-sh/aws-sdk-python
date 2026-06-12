"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Risk``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

"""<p>The risk for a given workload, lens review, pillar, or question.</p>"""
Risk: TypeAlias = Literal[
    "UNANSWERED",
    "HIGH",
    "MEDIUM",
    "NONE",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNANSWERED",
        "HIGH",
        "MEDIUM",
        "NONE",
        "NOT_APPLICABLE",
    )
)


def serialize_json(value: Risk) -> str:
    return value


def deserialize_json(data: str) -> Risk:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Risk value: {data!r}")
    return cast(Risk, data)
