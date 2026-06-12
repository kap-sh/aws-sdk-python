"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#WAFLoggingParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.logging_filter
    import aws_sdk_observabilityadmin.types.redacted_fields
    import aws_sdk_observabilityadmin.types.waf_log_type


class WAFLoggingParameters(TypedDict):
    redacted_fields: NotRequired[
        "aws_sdk_observabilityadmin.types.redacted_fields.RedactedFields"
    ]
    """<p> The fields to redact from WAF logs to protect sensitive information. </p>"""
    logging_filter: NotRequired[
        "aws_sdk_observabilityadmin.types.logging_filter.LoggingFilter"
    ]
    """<p> A filter configuration that determines which WAF log records to include or exclude. </p>"""
    log_type: NotRequired["aws_sdk_observabilityadmin.types.waf_log_type.WAFLogType"]
    """<p> The type of WAF logs to collect (currently supports WAF_LOGS). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WAFLoggingParameters) -> dict:
    out: dict = {}
    if "redacted_fields" in value:
        import aws_sdk_observabilityadmin.types.redacted_fields

        out["RedactedFields"] = (
            aws_sdk_observabilityadmin.types.redacted_fields.serialize_json(
                value["redacted_fields"]
            )
        )
    if "logging_filter" in value:
        import aws_sdk_observabilityadmin.types.logging_filter

        out["LoggingFilter"] = (
            aws_sdk_observabilityadmin.types.logging_filter.serialize_json(
                value["logging_filter"]
            )
        )
    if "log_type" in value:
        import aws_sdk_observabilityadmin.types.waf_log_type

        out["LogType"] = aws_sdk_observabilityadmin.types.waf_log_type.serialize_json(
            value["log_type"]
        )
    return out


def deserialize_json(data: dict) -> WAFLoggingParameters:
    out: WAFLoggingParameters = {}  # type: ignore[typeddict-item]
    if "RedactedFields" in data:
        import aws_sdk_observabilityadmin.types.redacted_fields

        out["redacted_fields"] = (
            aws_sdk_observabilityadmin.types.redacted_fields.deserialize_json(
                data["RedactedFields"]
            )
        )
    if "LoggingFilter" in data:
        import aws_sdk_observabilityadmin.types.logging_filter

        out["logging_filter"] = (
            aws_sdk_observabilityadmin.types.logging_filter.deserialize_json(
                data["LoggingFilter"]
            )
        )
    if "LogType" in data:
        import aws_sdk_observabilityadmin.types.waf_log_type

        out["log_type"] = (
            aws_sdk_observabilityadmin.types.waf_log_type.deserialize_json(
                data["LogType"]
            )
        )
    return out
