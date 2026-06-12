"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSStorageFinding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RDSStorageFinding: TypeAlias = Literal[
    "Optimized",
    "Underprovisioned",
    "Overprovisioned",
    "NotOptimized",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Optimized",
        "Underprovisioned",
        "Overprovisioned",
        "NotOptimized",
    )
)


def serialize_aws_json_1_0(value: RDSStorageFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSStorageFinding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RDSStorageFinding value: {data!r}")
    return cast(RDSStorageFinding, data)
