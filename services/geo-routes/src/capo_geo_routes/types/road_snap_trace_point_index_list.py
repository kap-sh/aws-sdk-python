"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTracePointIndexList``."""

from typing import TypeAlias

RoadSnapTracePointIndexList: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTracePointIndexList) -> list:
    return list(value)


def deserialize_json(data: list) -> RoadSnapTracePointIndexList:
    return list(data)
