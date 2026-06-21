"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionType``."""

from typing import Literal, TypeAlias, cast

AutomationRulesActionType: TypeAlias = Literal["FINDING_FIELDS_UPDATE",]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesActionType) -> str:
    return value


def deserialize_json(data: str) -> AutomationRulesActionType:
    return cast(AutomationRulesActionType, data)
