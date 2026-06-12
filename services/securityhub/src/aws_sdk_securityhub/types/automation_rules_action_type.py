"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

AutomationRulesActionType: TypeAlias = Literal["FINDING_FIELDS_UPDATE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FINDING_FIELDS_UPDATE",))


def serialize_json(value: AutomationRulesActionType) -> str:
    return value


def deserialize_json(data: str) -> AutomationRulesActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomationRulesActionType value: {data!r}")
    return cast(AutomationRulesActionType, data)
