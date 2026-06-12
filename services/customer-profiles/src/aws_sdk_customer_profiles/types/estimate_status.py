"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EstimateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

EstimateStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_json(value: EstimateStatus) -> str:
    return value


def deserialize_json(data: str) -> EstimateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EstimateStatus value: {data!r}")
    return cast(EstimateStatus, data)
