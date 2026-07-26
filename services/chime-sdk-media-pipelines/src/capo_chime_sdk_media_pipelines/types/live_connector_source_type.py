"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorSourceType``."""

from typing import Literal, TypeAlias, cast

LiveConnectorSourceType: TypeAlias = Literal["ChimeSdkMeeting",]


# --- restJson1 ser/de ---
def serialize_json(value: LiveConnectorSourceType) -> str:
    return value


def deserialize_json(data: str) -> LiveConnectorSourceType:
    return cast(LiveConnectorSourceType, data)
