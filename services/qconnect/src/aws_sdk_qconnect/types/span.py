"""Generated from Smithy shape ``com.amazonaws.qconnect#Span``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.span_attributes
    import aws_sdk_qconnect.types.span_status
    import aws_sdk_qconnect.types.span_type
    import aws_sdk_qconnect.types.uuid


class Span(TypedDict, closed=True):
    span_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>Unique span identifier</p>"""
    assistant_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>UUID of the Connect AI Assistant resource</p>"""
    session_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>UUID of the Connect AI Session resource</p>"""
    parent_span_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>Parent span identifier for hierarchy. Null for root spans.</p>"""
    span_name: "aws_sdk_qconnect.types.name.Name"
    """<p>Service-defined operation name</p>"""
    span_type: "aws_sdk_qconnect.types.span_type.SpanType"
    """<p>Operation relationship type</p>"""
    start_timestamp: "datetime.datetime"
    """<p>Operation start time in milliseconds since epoch</p>"""
    end_timestamp: "datetime.datetime"
    """<p>Operation end time in milliseconds since epoch</p>"""
    status: "aws_sdk_qconnect.types.span_status.SpanStatus"
    """<p>Span completion status</p>"""
    status_description: NotRequired[
        "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>Human-readable error description when status is ERROR or TIMEOUT</p>"""
    request_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The service request ID that initiated the operation</p>"""
    origin_request_id: NotRequired[
        "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>The origin request identifier for end-to-end tracing.</p>"""
    attributes: "aws_sdk_qconnect.types.span_attributes.SpanAttributes"
    """<p>Span-specific contextual attributes</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Span) -> dict:
    out: dict = {}
    out["spanId"] = value["span_id"]
    out["assistantId"] = value["assistant_id"]
    out["sessionId"] = value["session_id"]
    if "parent_span_id" in value:
        out["parentSpanId"] = value["parent_span_id"]
    out["spanName"] = value["span_name"]
    out["spanType"] = value["span_type"]
    import aws_sdk_qconnect.types._prelude.timestamp

    out["startTimestamp"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["start_timestamp"]
    )
    import aws_sdk_qconnect.types._prelude.timestamp

    out["endTimestamp"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["end_timestamp"]
    )
    out["status"] = value["status"]
    if "status_description" in value:
        out["statusDescription"] = value["status_description"]
    out["requestId"] = value["request_id"]
    if "origin_request_id" in value:
        out["originRequestId"] = value["origin_request_id"]
    import aws_sdk_qconnect.types.span_attributes

    out["attributes"] = aws_sdk_qconnect.types.span_attributes.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> Span:
    out: Span = {}  # type: ignore[typeddict-item]
    if "spanId" in data:
        out["span_id"] = data["spanId"]
    else:
        raise DeserializationError("Span.span_id required")
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("Span.assistant_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("Span.session_id required")
    if "parentSpanId" in data:
        out["parent_span_id"] = data["parentSpanId"]
    if "spanName" in data:
        out["span_name"] = data["spanName"]
    else:
        raise DeserializationError("Span.span_name required")
    if "spanType" in data:
        out["span_type"] = data["spanType"]
    else:
        raise DeserializationError("Span.span_type required")
    if "startTimestamp" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["start_timestamp"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["startTimestamp"]
            )
        )
    else:
        raise DeserializationError("Span.start_timestamp required")
    if "endTimestamp" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["end_timestamp"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["endTimestamp"]
            )
        )
    else:
        raise DeserializationError("Span.end_timestamp required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("Span.status required")
    if "statusDescription" in data:
        out["status_description"] = data["statusDescription"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("Span.request_id required")
    if "originRequestId" in data:
        out["origin_request_id"] = data["originRequestId"]
    if "attributes" in data:
        import aws_sdk_qconnect.types.span_attributes

        out["attributes"] = aws_sdk_qconnect.types.span_attributes.deserialize_json(
            data["attributes"]
        )
    else:
        raise DeserializationError("Span.attributes required")
    return out
