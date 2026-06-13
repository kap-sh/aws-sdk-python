"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveBudgetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

ServiceLevelObjectiveBudgetStatus: TypeAlias = Literal[
    "OK",
    "WARNING",
    "BREACHED",
    "INSUFFICIENT_DATA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "WARNING",
        "BREACHED",
        "INSUFFICIENT_DATA",
    )
)


def serialize_json(value: ServiceLevelObjectiveBudgetStatus) -> str:
    return value


def deserialize_json(data: str) -> ServiceLevelObjectiveBudgetStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceLevelObjectiveBudgetStatus value: {data!r}"
        )
    return cast(ServiceLevelObjectiveBudgetStatus, data)
