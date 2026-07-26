"""Generated from Smithy shape ``com.amazonaws.devopsagent#WebIdentityTokenAudienceList``."""

from typing import TypeAlias

WebIdentityTokenAudienceList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: WebIdentityTokenAudienceList) -> list:
    return list(value)


def deserialize_json(data: list) -> WebIdentityTokenAudienceList:
    return list(data)
