"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#TtlDurationUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_featurestore_runtime.errors import DeserializationError

TtlDurationUnit: TypeAlias = Literal[
    "Seconds",
    "Minutes",
    "Hours",
    "Days",
    "Weeks",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Seconds",
        "Minutes",
        "Hours",
        "Days",
        "Weeks",
    )
)


def serialize_json(value: TtlDurationUnit) -> str:
    return value


def deserialize_json(data: str) -> TtlDurationUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TtlDurationUnit value: {data!r}")
    return cast(TtlDurationUnit, data)
