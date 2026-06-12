"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

FleetAction: TypeAlias = Literal["AUTO_SCALING",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AUTO_SCALING",))


def serialize_aws_json_1_1(value: FleetAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetAction value: {data!r}")
    return cast(FleetAction, data)
