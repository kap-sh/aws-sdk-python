"""Generated from Smithy shape ``com.amazonaws.kendra#SlackEntity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

SlackEntity: TypeAlias = Literal[
    "PUBLIC_CHANNEL",
    "PRIVATE_CHANNEL",
    "GROUP_MESSAGE",
    "DIRECT_MESSAGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC_CHANNEL",
        "PRIVATE_CHANNEL",
        "GROUP_MESSAGE",
        "DIRECT_MESSAGE",
    )
)


def serialize_aws_json_1_1(value: SlackEntity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SlackEntity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlackEntity value: {data!r}")
    return cast(SlackEntity, data)
