"""Generated from Smithy shape ``com.amazonaws.pcs#SchedulerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

SchedulerType: TypeAlias = Literal["SLURM",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SLURM",))


def serialize_aws_json_1_0(value: SchedulerType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SchedulerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchedulerType value: {data!r}")
    return cast(SchedulerType, data)
