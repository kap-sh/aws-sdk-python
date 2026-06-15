"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LogGroupArnList``."""

from typing import TypeAlias

LogGroupArnList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> LogGroupArnList:
    return list(data)
