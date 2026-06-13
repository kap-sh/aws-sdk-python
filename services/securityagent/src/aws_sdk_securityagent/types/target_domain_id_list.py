"""Generated from Smithy shape ``com.amazonaws.securityagent#TargetDomainIdList``."""

from typing import TypeAlias

TargetDomainIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TargetDomainIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetDomainIdList:
    return list(data)
