"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ContainerGroupType: TypeAlias = Literal[
    "GAME_SERVER",
    "PER_INSTANCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GAME_SERVER",
        "PER_INSTANCE",
    )
)


def serialize_aws_json_1_1(value: ContainerGroupType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerGroupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerGroupType value: {data!r}")
    return cast(ContainerGroupType, data)
