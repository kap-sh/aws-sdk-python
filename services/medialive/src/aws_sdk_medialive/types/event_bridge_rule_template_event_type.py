"""Generated from Smithy shape ``com.amazonaws.medialive#EventBridgeRuleTemplateEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The type of event to match with the rule."""
EventBridgeRuleTemplateEventType: TypeAlias = Literal[
    "MEDIALIVE_MULTIPLEX_ALERT",
    "MEDIALIVE_MULTIPLEX_STATE_CHANGE",
    "MEDIALIVE_CHANNEL_ALERT",
    "MEDIALIVE_CHANNEL_INPUT_CHANGE",
    "MEDIALIVE_CHANNEL_STATE_CHANGE",
    "MEDIAPACKAGE_INPUT_NOTIFICATION",
    "MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION",
    "MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION",
    "SIGNAL_MAP_ACTIVE_ALARM",
    "MEDIACONNECT_ALERT",
    "MEDIACONNECT_SOURCE_HEALTH",
    "MEDIACONNECT_OUTPUT_HEALTH",
    "MEDIACONNECT_FLOW_STATUS_CHANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MEDIALIVE_MULTIPLEX_ALERT",
        "MEDIALIVE_MULTIPLEX_STATE_CHANGE",
        "MEDIALIVE_CHANNEL_ALERT",
        "MEDIALIVE_CHANNEL_INPUT_CHANGE",
        "MEDIALIVE_CHANNEL_STATE_CHANGE",
        "MEDIAPACKAGE_INPUT_NOTIFICATION",
        "MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION",
        "MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION",
        "SIGNAL_MAP_ACTIVE_ALARM",
        "MEDIACONNECT_ALERT",
        "MEDIACONNECT_SOURCE_HEALTH",
        "MEDIACONNECT_OUTPUT_HEALTH",
        "MEDIACONNECT_FLOW_STATUS_CHANGE",
    )
)


def serialize_json(value: EventBridgeRuleTemplateEventType) -> str:
    return value


def deserialize_json(data: str) -> EventBridgeRuleTemplateEventType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EventBridgeRuleTemplateEventType value: {data!r}"
        )
    return cast(EventBridgeRuleTemplateEventType, data)
