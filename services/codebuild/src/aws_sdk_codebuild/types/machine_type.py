"""Generated from Smithy shape ``com.amazonaws.codebuild#MachineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

MachineType: TypeAlias = Literal[
    "GENERAL",
    "NVME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GENERAL",
        "NVME",
    )
)


def serialize_aws_json_1_1(value: MachineType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MachineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MachineType value: {data!r}")
    return cast(MachineType, data)
