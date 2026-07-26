"""Generated from Smithy shape ``com.amazonaws.polly#EngineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_polly.types.engine

EngineList: TypeAlias = list["capo_polly.types.engine.Engine"]


# --- restJson1 ser/de ---
def serialize_json(value: EngineList) -> list:
    import capo_polly.types.engine

    out: list = []
    for item in value:
        out.append(capo_polly.types.engine.serialize_json(item))
    return out


def deserialize_json(data: list) -> EngineList:
    import capo_polly.types.engine

    out: EngineList = []
    for item in data:
        out.append(capo_polly.types.engine.deserialize_json(item))
    return out
