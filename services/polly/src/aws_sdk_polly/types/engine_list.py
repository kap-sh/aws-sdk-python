"""Generated from Smithy shape ``com.amazonaws.polly#EngineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_polly.types.engine

EngineList: TypeAlias = list["aws_sdk_polly.types.engine.Engine"]


# --- restJson1 ser/de ---
def serialize_json(value: EngineList) -> list:
    import aws_sdk_polly.types.engine

    out: list = []
    for item in value:
        out.append(aws_sdk_polly.types.engine.serialize_json(item))
    return out


def deserialize_json(data: list) -> EngineList:
    import aws_sdk_polly.types.engine

    out: EngineList = []
    for item in data:
        out.append(aws_sdk_polly.types.engine.deserialize_json(item))
    return out
