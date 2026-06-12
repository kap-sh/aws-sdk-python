"""Generated from Smithy shape ``com.amazonaws.sustainability#Dimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sustainability.errors import DeserializationError

"""<p>Specifies the dimensions available for grouping and filtering emissions data.</p>"""
Dimension: TypeAlias = Literal[
    "USAGE_ACCOUNT_ID",
    "REGION",
    "SERVICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USAGE_ACCOUNT_ID",
        "REGION",
        "SERVICE",
    )
)


def serialize_json(value: Dimension) -> str:
    return value


def deserialize_json(data: str) -> Dimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Dimension value: {data!r}")
    return cast(Dimension, data)
