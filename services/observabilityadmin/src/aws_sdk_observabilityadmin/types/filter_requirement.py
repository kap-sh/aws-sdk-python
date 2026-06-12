"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#FilterRequirement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

"""<p> Enumeration of condition matching requirements: MEETS_ALL requires all conditions to match, MEETS_ANY requires at least one. </p>"""
FilterRequirement: TypeAlias = Literal[
    "MEETS_ALL",
    "MEETS_ANY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MEETS_ALL",
        "MEETS_ANY",
    )
)


def serialize_json(value: FilterRequirement) -> str:
    return value


def deserialize_json(data: str) -> FilterRequirement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterRequirement value: {data!r}")
    return cast(FilterRequirement, data)
