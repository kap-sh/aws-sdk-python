"""Generated from Smithy shape ``com.amazonaws.devopsagent#PagerDutyScopes``."""

from typing import TypeAlias

PagerDutyScopes: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyScopes) -> list:
    return list(value)


def deserialize_json(data: list) -> PagerDutyScopes:
    return list(data)
