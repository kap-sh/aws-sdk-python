"""Generated from Smithy shape ``com.amazonaws.iot#FleetIndexingApi``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

FleetIndexingApi: TypeAlias = Literal["GET_THING_CONNECTIVITY_DATA",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GET_THING_CONNECTIVITY_DATA",))


def serialize_json(value: FleetIndexingApi) -> str:
    return value


def deserialize_json(data: str) -> FleetIndexingApi:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetIndexingApi value: {data!r}")
    return cast(FleetIndexingApi, data)
