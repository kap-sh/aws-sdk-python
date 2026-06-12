"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Finding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

Finding: TypeAlias = Literal[
    "Underprovisioned",
    "Overprovisioned",
    "Optimized",
    "NotOptimized",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Underprovisioned",
        "Overprovisioned",
        "Optimized",
        "NotOptimized",
    )
)


def serialize_aws_json_1_0(value: Finding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Finding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Finding value: {data!r}")
    return cast(Finding, data)
