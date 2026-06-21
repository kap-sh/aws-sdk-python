"""Generated from Smithy shape ``com.amazonaws.iot#FleetIndexingApi``."""

from typing import Literal, TypeAlias, cast

FleetIndexingApi: TypeAlias = Literal["GET_THING_CONNECTIVITY_DATA",]


# --- restJson1 ser/de ---
def serialize_json(value: FleetIndexingApi) -> str:
    return value


def deserialize_json(data: str) -> FleetIndexingApi:
    return cast(FleetIndexingApi, data)
