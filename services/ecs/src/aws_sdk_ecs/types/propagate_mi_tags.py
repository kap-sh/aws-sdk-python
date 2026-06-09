"""Generated from Smithy shape ``com.amazonaws.ecs#PropagateMITags``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

PropagateMITags: TypeAlias = Literal[
    "CAPACITY_PROVIDER",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CAPACITY_PROVIDER",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: PropagateMITags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropagateMITags:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropagateMITags value: {data!r}")
    return cast(PropagateMITags, data)
