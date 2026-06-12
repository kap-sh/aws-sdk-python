"""Generated from Smithy shape ``com.amazonaws.appflow#GoogleAnalyticsConnectorOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

GoogleAnalyticsConnectorOperator: TypeAlias = Literal[
    "PROJECTION",
    "BETWEEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROJECTION",
        "BETWEEN",
    )
)


def serialize_json(value: GoogleAnalyticsConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> GoogleAnalyticsConnectorOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GoogleAnalyticsConnectorOperator value: {data!r}"
        )
    return cast(GoogleAnalyticsConnectorOperator, data)
