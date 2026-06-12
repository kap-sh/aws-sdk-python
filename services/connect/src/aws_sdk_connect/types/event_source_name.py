"""Generated from Smithy shape ``com.amazonaws.connect#EventSourceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EventSourceName: TypeAlias = Literal[
    "OnPostCallAnalysisAvailable",
    "OnRealTimeCallAnalysisAvailable",
    "OnRealTimeChatAnalysisAvailable",
    "OnPostChatAnalysisAvailable",
    "OnEmailAnalysisAvailable",
    "OnZendeskTicketCreate",
    "OnZendeskTicketStatusUpdate",
    "OnSalesforceCaseCreate",
    "OnContactEvaluationSubmit",
    "OnMetricDataUpdate",
    "OnCaseCreate",
    "OnCaseUpdate",
    "OnSlaBreach",
    "OnAlertUpdate",
    "OnSchedulePublish",
    "OnScheduleUpdate",
    "OnScheduleTimeOffRequestActivity",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OnPostCallAnalysisAvailable",
        "OnRealTimeCallAnalysisAvailable",
        "OnRealTimeChatAnalysisAvailable",
        "OnPostChatAnalysisAvailable",
        "OnEmailAnalysisAvailable",
        "OnZendeskTicketCreate",
        "OnZendeskTicketStatusUpdate",
        "OnSalesforceCaseCreate",
        "OnContactEvaluationSubmit",
        "OnMetricDataUpdate",
        "OnCaseCreate",
        "OnCaseUpdate",
        "OnSlaBreach",
        "OnAlertUpdate",
        "OnSchedulePublish",
        "OnScheduleUpdate",
        "OnScheduleTimeOffRequestActivity",
    )
)


def serialize_json(value: EventSourceName) -> str:
    return value


def deserialize_json(data: str) -> EventSourceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSourceName value: {data!r}")
    return cast(EventSourceName, data)
