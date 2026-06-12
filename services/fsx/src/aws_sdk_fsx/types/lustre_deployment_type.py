"""Generated from Smithy shape ``com.amazonaws.fsx#LustreDeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

LustreDeploymentType: TypeAlias = Literal[
    "SCRATCH_1",
    "SCRATCH_2",
    "PERSISTENT_1",
    "PERSISTENT_2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCRATCH_1",
        "SCRATCH_2",
        "PERSISTENT_1",
        "PERSISTENT_2",
    )
)


def serialize_aws_json_1_1(value: LustreDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LustreDeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LustreDeploymentType value: {data!r}")
    return cast(LustreDeploymentType, data)
