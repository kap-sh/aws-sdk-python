"""Generated from Smithy shape ``com.amazonaws.shield#SubResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

SubResourceType: TypeAlias = Literal[
    "IP",
    "URL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IP",
        "URL",
    )
)


def serialize_aws_json_1_1(value: SubResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubResourceType value: {data!r}")
    return cast(SubResourceType, data)
