"""Generated from Smithy shape ``com.amazonaws.connect#HistoricalMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The historical metric names.</p>"""
HistoricalMetricName: TypeAlias = Literal[
    "CONTACTS_QUEUED",
    "CONTACTS_HANDLED",
    "CONTACTS_ABANDONED",
    "CONTACTS_CONSULTED",
    "CONTACTS_AGENT_HUNG_UP_FIRST",
    "CONTACTS_HANDLED_INCOMING",
    "CONTACTS_HANDLED_OUTBOUND",
    "CONTACTS_HOLD_ABANDONS",
    "CONTACTS_TRANSFERRED_IN",
    "CONTACTS_TRANSFERRED_OUT",
    "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
    "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
    "CONTACTS_MISSED",
    "CALLBACK_CONTACTS_HANDLED",
    "API_CONTACTS_HANDLED",
    "OCCUPANCY",
    "HANDLE_TIME",
    "AFTER_CONTACT_WORK_TIME",
    "QUEUED_TIME",
    "ABANDON_TIME",
    "QUEUE_ANSWER_TIME",
    "HOLD_TIME",
    "INTERACTION_TIME",
    "INTERACTION_AND_HOLD_TIME",
    "SERVICE_LEVEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTACTS_QUEUED",
        "CONTACTS_HANDLED",
        "CONTACTS_ABANDONED",
        "CONTACTS_CONSULTED",
        "CONTACTS_AGENT_HUNG_UP_FIRST",
        "CONTACTS_HANDLED_INCOMING",
        "CONTACTS_HANDLED_OUTBOUND",
        "CONTACTS_HOLD_ABANDONS",
        "CONTACTS_TRANSFERRED_IN",
        "CONTACTS_TRANSFERRED_OUT",
        "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
        "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
        "CONTACTS_MISSED",
        "CALLBACK_CONTACTS_HANDLED",
        "API_CONTACTS_HANDLED",
        "OCCUPANCY",
        "HANDLE_TIME",
        "AFTER_CONTACT_WORK_TIME",
        "QUEUED_TIME",
        "ABANDON_TIME",
        "QUEUE_ANSWER_TIME",
        "HOLD_TIME",
        "INTERACTION_TIME",
        "INTERACTION_AND_HOLD_TIME",
        "SERVICE_LEVEL",
    )
)


def serialize_json(value: HistoricalMetricName) -> str:
    return value


def deserialize_json(data: str) -> HistoricalMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HistoricalMetricName value: {data!r}")
    return cast(HistoricalMetricName, data)
