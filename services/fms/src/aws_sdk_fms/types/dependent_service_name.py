"""Generated from Smithy shape ``com.amazonaws.fms#DependentServiceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

DependentServiceName: TypeAlias = Literal[
    "AWSCONFIG",
    "AWSWAF",
    "AWSSHIELD_ADVANCED",
    "AWSVPC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWSCONFIG",
        "AWSWAF",
        "AWSSHIELD_ADVANCED",
        "AWSVPC",
    )
)


def serialize_aws_json_1_1(value: DependentServiceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DependentServiceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DependentServiceName value: {data!r}")
    return cast(DependentServiceName, data)
