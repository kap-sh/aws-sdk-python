"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#FilterBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

"""<p> Enumeration of filter actions: KEEP to include log records, DROP to exclude them. </p>"""
FilterBehavior: TypeAlias = Literal[
    "KEEP",
    "DROP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEEP",
        "DROP",
    )
)


def serialize_json(value: FilterBehavior) -> str:
    return value


def deserialize_json(data: str) -> FilterBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterBehavior value: {data!r}")
    return cast(FilterBehavior, data)
