"""Generated from Smithy shape ``com.amazonaws.devopsagent#PagerDutyScopesList``."""

from typing import TypeAlias

PagerDutyScopesList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyScopesList) -> list:
    return list(value)


def deserialize_json(data: list) -> PagerDutyScopesList:
    return list(data)
