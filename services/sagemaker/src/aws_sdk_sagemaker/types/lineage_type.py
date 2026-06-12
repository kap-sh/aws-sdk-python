"""Generated from Smithy shape ``com.amazonaws.sagemaker#LineageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

LineageType: TypeAlias = Literal[
    "TrialComponent",
    "Artifact",
    "Context",
    "Action",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TrialComponent",
        "Artifact",
        "Context",
        "Action",
    )
)


def serialize_aws_json_1_1(value: LineageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LineageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineageType value: {data!r}")
    return cast(LineageType, data)
