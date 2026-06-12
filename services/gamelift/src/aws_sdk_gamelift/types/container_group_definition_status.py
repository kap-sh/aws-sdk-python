"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupDefinitionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ContainerGroupDefinitionStatus: TypeAlias = Literal[
    "READY",
    "COPYING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "COPYING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ContainerGroupDefinitionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerGroupDefinitionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContainerGroupDefinitionStatus value: {data!r}"
        )
    return cast(ContainerGroupDefinitionStatus, data)
