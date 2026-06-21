"""Generated from Smithy shape ``com.amazonaws.connect#EventSourceName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: EventSourceName) -> str:
    return value


def deserialize_json(data: str) -> EventSourceName:
    return cast(EventSourceName, data)
