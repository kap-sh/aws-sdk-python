"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMaskingForHttpCode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.responder_error_masking_action
    import aws_sdk_rtbfabric.types.responder_error_masking_logging_types


class ResponderErrorMaskingForHttpCode(TypedDict):
    http_code: "str"
    """<p>The HTTP error code.</p>"""
    action: "aws_sdk_rtbfabric.types.responder_error_masking_action.ResponderErrorMaskingAction"
    """<p>The action for the error..</p>"""
    logging_types: "aws_sdk_rtbfabric.types.responder_error_masking_logging_types.ResponderErrorMaskingLoggingTypes"
    """<p>The error log type.</p>"""
    response_logging_percentage: NotRequired["float"]
    """<p>The percentage of response logging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponderErrorMaskingForHttpCode) -> dict:
    out: dict = {}
    out["httpCode"] = value["http_code"]
    import aws_sdk_rtbfabric.types.responder_error_masking_action

    out["action"] = (
        aws_sdk_rtbfabric.types.responder_error_masking_action.serialize_json(
            value["action"]
        )
    )
    import aws_sdk_rtbfabric.types.responder_error_masking_logging_types

    out["loggingTypes"] = (
        aws_sdk_rtbfabric.types.responder_error_masking_logging_types.serialize_json(
            value["logging_types"]
        )
    )
    if "response_logging_percentage" in value:
        out["responseLoggingPercentage"] = value["response_logging_percentage"]
    return out


def deserialize_json(data: dict) -> ResponderErrorMaskingForHttpCode:
    out: ResponderErrorMaskingForHttpCode = {}  # type: ignore[typeddict-item]
    if "httpCode" in data:
        out["http_code"] = data["httpCode"]
    else:
        raise DeserializationError(
            "ResponderErrorMaskingForHttpCode.http_code required"
        )
    if "action" in data:
        import aws_sdk_rtbfabric.types.responder_error_masking_action

        out["action"] = (
            aws_sdk_rtbfabric.types.responder_error_masking_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("ResponderErrorMaskingForHttpCode.action required")
    if "loggingTypes" in data:
        import aws_sdk_rtbfabric.types.responder_error_masking_logging_types

        out["logging_types"] = (
            aws_sdk_rtbfabric.types.responder_error_masking_logging_types.deserialize_json(
                data["loggingTypes"]
            )
        )
    else:
        raise DeserializationError(
            "ResponderErrorMaskingForHttpCode.logging_types required"
        )
    if "responseLoggingPercentage" in data:
        out["response_logging_percentage"] = data["responseLoggingPercentage"]
    return out
