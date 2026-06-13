"""Generated from Smithy shape ``com.amazonaws.securityagent#FindingIdList``."""

from typing import TypeAlias

FindingIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> FindingIdList:
    return list(data)
