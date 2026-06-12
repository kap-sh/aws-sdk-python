"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseFinding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LicenseFinding: TypeAlias = Literal[
    "InsufficientMetrics",
    "Optimized",
    "NotOptimized",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InsufficientMetrics",
        "Optimized",
        "NotOptimized",
    )
)


def serialize_aws_json_1_0(value: LicenseFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseFinding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseFinding value: {data!r}")
    return cast(LicenseFinding, data)
