"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

StepType: TypeAlias = Literal[
    "CreateEbsSnapshot",
    "DeleteEbsVolume",
    "ModifyEbsVolume",
    "CreateEbsVolume",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreateEbsSnapshot",
        "DeleteEbsVolume",
        "ModifyEbsVolume",
        "CreateEbsVolume",
    )
)


def serialize_aws_json_1_0(value: StepType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StepType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepType value: {data!r}")
    return cast(StepType, data)
