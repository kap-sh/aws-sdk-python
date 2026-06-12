"""Generated from Smithy shape ``com.amazonaws.codedeploy#ApplicationRevisionSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

ApplicationRevisionSortBy: TypeAlias = Literal[
    "registerTime",
    "firstUsedTime",
    "lastUsedTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "registerTime",
        "firstUsedTime",
        "lastUsedTime",
    )
)


def serialize_aws_json_1_1(value: ApplicationRevisionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationRevisionSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationRevisionSortBy value: {data!r}")
    return cast(ApplicationRevisionSortBy, data)
