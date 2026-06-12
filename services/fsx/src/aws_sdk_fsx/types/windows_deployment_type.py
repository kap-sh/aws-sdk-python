"""Generated from Smithy shape ``com.amazonaws.fsx#WindowsDeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

WindowsDeploymentType: TypeAlias = Literal[
    "MULTI_AZ_1",
    "SINGLE_AZ_1",
    "SINGLE_AZ_2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MULTI_AZ_1",
        "SINGLE_AZ_1",
        "SINGLE_AZ_2",
    )
)


def serialize_aws_json_1_1(value: WindowsDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WindowsDeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WindowsDeploymentType value: {data!r}")
    return cast(WindowsDeploymentType, data)
