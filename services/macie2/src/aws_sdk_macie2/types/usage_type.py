"""Generated from Smithy shape ``com.amazonaws.macie2#UsageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The name of an Amazon Macie usage metric for an account. Possible values are:</p>"""
UsageType: TypeAlias = Literal[
    "DATA_INVENTORY_EVALUATION",
    "SENSITIVE_DATA_DISCOVERY",
    "AUTOMATED_SENSITIVE_DATA_DISCOVERY",
    "AUTOMATED_OBJECT_MONITORING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATA_INVENTORY_EVALUATION",
        "SENSITIVE_DATA_DISCOVERY",
        "AUTOMATED_SENSITIVE_DATA_DISCOVERY",
        "AUTOMATED_OBJECT_MONITORING",
    )
)


def serialize_json(value: UsageType) -> str:
    return value


def deserialize_json(data: str) -> UsageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageType value: {data!r}")
    return cast(UsageType, data)
