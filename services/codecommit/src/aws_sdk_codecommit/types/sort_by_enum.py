"""Generated from Smithy shape ``com.amazonaws.codecommit#SortByEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

SortByEnum: TypeAlias = Literal[
    "repositoryName",
    "lastModifiedDate",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "repositoryName",
        "lastModifiedDate",
    )
)


def serialize_aws_json_1_1(value: SortByEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortByEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortByEnum value: {data!r}")
    return cast(SortByEnum, data)
