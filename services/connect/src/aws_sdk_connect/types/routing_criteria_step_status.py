"""Generated from Smithy shape ``com.amazonaws.connect#RoutingCriteriaStepStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RoutingCriteriaStepStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "JOINED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "JOINED",
        "EXPIRED",
    )
)


def serialize_json(value: RoutingCriteriaStepStatus) -> str:
    return value


def deserialize_json(data: str) -> RoutingCriteriaStepStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingCriteriaStepStatus value: {data!r}")
    return cast(RoutingCriteriaStepStatus, data)
