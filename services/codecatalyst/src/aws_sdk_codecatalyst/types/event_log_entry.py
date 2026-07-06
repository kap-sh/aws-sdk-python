"""Generated from Smithy shape ``com.amazonaws.codecatalyst#EventLogEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.event_payload
    import aws_sdk_codecatalyst.types.operation_type
    import aws_sdk_codecatalyst.types.project_information
    import aws_sdk_codecatalyst.types.timestamp
    import aws_sdk_codecatalyst.types.user_identity


class EventLogEntry(TypedDict, closed=True):
    id: "str"
    """<p>The system-generated unique ID of the event.</p>"""
    event_name: "str"
    """<p>The name of the event.</p>"""
    event_type: "str"
    """<p>The type of the event.</p>"""
    event_category: "str"
    """<p>The category for the event.</p>"""
    event_source: "str"
    """<p>The source of the event.</p>"""
    event_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The time the event took place, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""
    operation_type: "aws_sdk_codecatalyst.types.operation_type.OperationType"
    """<p>The type of the event.</p>"""
    user_identity: "aws_sdk_codecatalyst.types.user_identity.UserIdentity"
    """<p>The system-generated unique ID of the user whose actions are recorded in the event.</p>"""
    project_information: NotRequired[
        "aws_sdk_codecatalyst.types.project_information.ProjectInformation"
    ]
    """<p>Information about the project where the event occurred.</p>"""
    request_id: NotRequired["str"]
    """<p>The system-generated unique ID of the request.</p>"""
    request_payload: NotRequired[
        "aws_sdk_codecatalyst.types.event_payload.EventPayload"
    ]
    """<p>Information about the payload of the request.</p>"""
    response_payload: NotRequired[
        "aws_sdk_codecatalyst.types.event_payload.EventPayload"
    ]
    """<p>Information about the payload of the response, if any.</p>"""
    error_code: NotRequired["str"]
    """<p>The code of the error, if any.</p>"""
    source_ip_address: NotRequired["str"]
    """<p>The IP address of the user whose actions are recorded in the event.</p>"""
    user_agent: NotRequired["str"]
    """<p>The user agent whose actions are recorded in the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventLogEntry) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["eventName"] = value["event_name"]
    out["eventType"] = value["event_type"]
    out["eventCategory"] = value["event_category"]
    out["eventSource"] = value["event_source"]
    import aws_sdk_codecatalyst.types.timestamp

    out["eventTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["event_time"]
    )
    out["operationType"] = value["operation_type"]
    import aws_sdk_codecatalyst.types.user_identity

    out["userIdentity"] = aws_sdk_codecatalyst.types.user_identity.serialize_json(
        value["user_identity"]
    )
    if "project_information" in value:
        import aws_sdk_codecatalyst.types.project_information

        out["projectInformation"] = (
            aws_sdk_codecatalyst.types.project_information.serialize_json(
                value["project_information"]
            )
        )
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "request_payload" in value:
        import aws_sdk_codecatalyst.types.event_payload

        out["requestPayload"] = aws_sdk_codecatalyst.types.event_payload.serialize_json(
            value["request_payload"]
        )
    if "response_payload" in value:
        import aws_sdk_codecatalyst.types.event_payload

        out["responsePayload"] = (
            aws_sdk_codecatalyst.types.event_payload.serialize_json(
                value["response_payload"]
            )
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "source_ip_address" in value:
        out["sourceIpAddress"] = value["source_ip_address"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    return out


def deserialize_json(data: dict) -> EventLogEntry:
    out: EventLogEntry = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("EventLogEntry.id required")
    if "eventName" in data:
        out["event_name"] = data["eventName"]
    else:
        raise DeserializationError("EventLogEntry.event_name required")
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("EventLogEntry.event_type required")
    if "eventCategory" in data:
        out["event_category"] = data["eventCategory"]
    else:
        raise DeserializationError("EventLogEntry.event_category required")
    if "eventSource" in data:
        out["event_source"] = data["eventSource"]
    else:
        raise DeserializationError("EventLogEntry.event_source required")
    if "eventTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["event_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["eventTime"]
        )
    else:
        raise DeserializationError("EventLogEntry.event_time required")
    if "operationType" in data:
        out["operation_type"] = data["operationType"]
    else:
        raise DeserializationError("EventLogEntry.operation_type required")
    if "userIdentity" in data:
        import aws_sdk_codecatalyst.types.user_identity

        out["user_identity"] = (
            aws_sdk_codecatalyst.types.user_identity.deserialize_json(
                data["userIdentity"]
            )
        )
    else:
        raise DeserializationError("EventLogEntry.user_identity required")
    if "projectInformation" in data:
        import aws_sdk_codecatalyst.types.project_information

        out["project_information"] = (
            aws_sdk_codecatalyst.types.project_information.deserialize_json(
                data["projectInformation"]
            )
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "requestPayload" in data:
        import aws_sdk_codecatalyst.types.event_payload

        out["request_payload"] = (
            aws_sdk_codecatalyst.types.event_payload.deserialize_json(
                data["requestPayload"]
            )
        )
    if "responsePayload" in data:
        import aws_sdk_codecatalyst.types.event_payload

        out["response_payload"] = (
            aws_sdk_codecatalyst.types.event_payload.deserialize_json(
                data["responsePayload"]
            )
        )
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "sourceIpAddress" in data:
        out["source_ip_address"] = data["sourceIpAddress"]
    if "userAgent" in data:
        out["user_agent"] = data["userAgent"]
    return out
