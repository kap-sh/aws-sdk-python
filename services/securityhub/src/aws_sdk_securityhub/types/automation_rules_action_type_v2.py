"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionTypeV2``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

AutomationRulesActionTypeV2: TypeAlias = Literal[
    "FINDING_FIELDS_UPDATE",
    "EXTERNAL_INTEGRATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FINDING_FIELDS_UPDATE",
        "EXTERNAL_INTEGRATION",
    )
)


def serialize_json(value: AutomationRulesActionTypeV2) -> str:
    return value


def deserialize_json(data: str) -> AutomationRulesActionTypeV2:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomationRulesActionTypeV2 value: {data!r}"
        )
    return cast(AutomationRulesActionTypeV2, data)
