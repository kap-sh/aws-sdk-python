"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetRemoveAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ContainerFleetRemoveAttribute: TypeAlias = Literal[
    "PER_INSTANCE_CONTAINER_GROUP_DEFINITION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PER_INSTANCE_CONTAINER_GROUP_DEFINITION",))


def serialize_aws_json_1_1(value: ContainerFleetRemoveAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerFleetRemoveAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContainerFleetRemoveAttribute value: {data!r}"
        )
    return cast(ContainerFleetRemoveAttribute, data)
