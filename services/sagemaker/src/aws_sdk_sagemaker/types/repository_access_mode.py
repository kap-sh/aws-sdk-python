"""Generated from Smithy shape ``com.amazonaws.sagemaker#RepositoryAccessMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RepositoryAccessMode: TypeAlias = Literal[
    "Platform",
    "Vpc",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Platform",
        "Vpc",
    )
)


def serialize_aws_json_1_1(value: RepositoryAccessMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RepositoryAccessMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RepositoryAccessMode value: {data!r}")
    return cast(RepositoryAccessMode, data)
