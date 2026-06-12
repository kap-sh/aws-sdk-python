"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSFinding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

EBSFinding: TypeAlias = Literal[
    "Optimized",
    "NotOptimized",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Optimized",
        "NotOptimized",
    )
)


def serialize_aws_json_1_0(value: EBSFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EBSFinding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EBSFinding value: {data!r}")
    return cast(EBSFinding, data)
