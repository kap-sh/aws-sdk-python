"""Generated from Smithy shape ``com.amazonaws.devopsagent#NewRelicEntityGuids``."""

from typing import TypeAlias

NewRelicEntityGuids: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: NewRelicEntityGuids) -> list:
    return list(value)


def deserialize_json(data: list) -> NewRelicEntityGuids:
    return list(data)
