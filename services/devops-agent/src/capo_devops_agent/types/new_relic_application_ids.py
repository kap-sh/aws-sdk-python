"""Generated from Smithy shape ``com.amazonaws.devopsagent#NewRelicApplicationIds``."""

from typing import TypeAlias

NewRelicApplicationIds: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: NewRelicApplicationIds) -> list:
    return list(value)


def deserialize_json(data: list) -> NewRelicApplicationIds:
    return list(data)
