"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleFinding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

IdleFinding: TypeAlias = Literal[
    "Idle",
    "Unattached",
    "Unused",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Idle",
        "Unattached",
        "Unused",
    )
)


def serialize_aws_json_1_0(value: IdleFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdleFinding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdleFinding value: {data!r}")
    return cast(IdleFinding, data)
