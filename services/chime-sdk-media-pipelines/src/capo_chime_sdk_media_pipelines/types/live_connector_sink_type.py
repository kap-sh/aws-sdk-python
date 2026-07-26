"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorSinkType``."""

from typing import Literal, TypeAlias, cast

LiveConnectorSinkType: TypeAlias = Literal["RTMP",]


# --- restJson1 ser/de ---
def serialize_json(value: LiveConnectorSinkType) -> str:
    return value


def deserialize_json(data: str) -> LiveConnectorSinkType:
    return cast(LiveConnectorSinkType, data)
