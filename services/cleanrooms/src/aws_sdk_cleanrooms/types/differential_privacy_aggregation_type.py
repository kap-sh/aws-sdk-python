"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyAggregationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

DifferentialPrivacyAggregationType: TypeAlias = Literal[
    "AVG",
    "COUNT",
    "COUNT_DISTINCT",
    "SUM",
    "STDDEV",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVG",
        "COUNT",
        "COUNT_DISTINCT",
        "SUM",
        "STDDEV",
    )
)


def serialize_json(value: DifferentialPrivacyAggregationType) -> str:
    return value


def deserialize_json(data: str) -> DifferentialPrivacyAggregationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DifferentialPrivacyAggregationType value: {data!r}"
        )
    return cast(DifferentialPrivacyAggregationType, data)
