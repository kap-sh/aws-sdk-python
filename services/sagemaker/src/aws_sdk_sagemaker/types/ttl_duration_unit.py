"""Generated from Smithy shape ``com.amazonaws.sagemaker#TtlDurationUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TtlDurationUnit: TypeAlias = Literal[
    "Seconds",
    "Minutes",
    "Hours",
    "Days",
    "Weeks",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Seconds",
        "Minutes",
        "Hours",
        "Days",
        "Weeks",
    )
)


def serialize_aws_json_1_1(value: TtlDurationUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TtlDurationUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TtlDurationUnit value: {data!r}")
    return cast(TtlDurationUnit, data)
