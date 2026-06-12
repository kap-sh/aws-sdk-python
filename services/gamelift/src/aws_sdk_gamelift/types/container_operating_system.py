"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerOperatingSystem``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ContainerOperatingSystem: TypeAlias = Literal["AMAZON_LINUX_2023",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AMAZON_LINUX_2023",))


def serialize_aws_json_1_1(value: ContainerOperatingSystem) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerOperatingSystem:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerOperatingSystem value: {data!r}")
    return cast(ContainerOperatingSystem, data)
