"""Generated from Smithy shape ``com.amazonaws.codepipeline#FailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

FailureType: TypeAlias = Literal[
    "JobFailed",
    "ConfigurationError",
    "PermissionError",
    "RevisionOutOfSync",
    "RevisionUnavailable",
    "SystemUnavailable",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JobFailed",
        "ConfigurationError",
        "PermissionError",
        "RevisionOutOfSync",
        "RevisionUnavailable",
        "SystemUnavailable",
    )
)


def serialize_aws_json_1_1(value: FailureType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailureType value: {data!r}")
    return cast(FailureType, data)
