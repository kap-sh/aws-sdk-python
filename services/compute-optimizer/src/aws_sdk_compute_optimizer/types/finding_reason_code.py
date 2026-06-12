"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#FindingReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

FindingReasonCode: TypeAlias = Literal[
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MemoryOverprovisioned",
        "MemoryUnderprovisioned",
    )
)


def serialize_aws_json_1_0(value: FindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FindingReasonCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingReasonCode value: {data!r}")
    return cast(FindingReasonCode, data)
