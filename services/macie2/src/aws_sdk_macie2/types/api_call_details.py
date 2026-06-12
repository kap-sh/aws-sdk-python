"""Generated from Smithy shape ``com.amazonaws.macie2#ApiCallDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601


class ApiCallDetails(TypedDict):
    api: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the operation that was invoked most recently and produced the finding.</p>"""
    api_service_name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The URL of the Amazon Web Services service that provides the operation, for example: s3.amazonaws.com.</p>"""
    first_seen: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The first date and time, in UTC and extended ISO 8601 format, when any operation was invoked and produced the finding.</p>"""
    last_seen: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The most recent date and time, in UTC and extended ISO 8601 format, when the specified operation (api) was invoked and produced the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiCallDetails) -> dict:
    out: dict = {}
    if "api" in value:
        out["api"] = value["api"]
    if "api_service_name" in value:
        out["apiServiceName"] = value["api_service_name"]
    if "first_seen" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["firstSeen"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["first_seen"]
        )
    if "last_seen" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["lastSeen"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["last_seen"]
        )
    return out


def deserialize_json(data: dict) -> ApiCallDetails:
    out: ApiCallDetails = {}  # type: ignore[typeddict-item]
    if "api" in data:
        out["api"] = data["api"]
    if "apiServiceName" in data:
        out["api_service_name"] = data["apiServiceName"]
    if "firstSeen" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["first_seen"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["firstSeen"]
        )
    if "lastSeen" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["last_seen"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["lastSeen"]
        )
    return out
