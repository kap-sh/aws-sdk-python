"""Generated from Smithy shape ``com.amazonaws.inspector#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.access_denied_error_code
    import aws_sdk_inspector.types.bool
    import aws_sdk_inspector.types.error_message


class AccessDeniedException_(TypedDict):
    message: "aws_sdk_inspector.types.error_message.ErrorMessage"
    """<p>Details of the exception error.</p>"""
    error_code: "aws_sdk_inspector.types.access_denied_error_code.AccessDeniedErrorCode"
    """<p>Code that indicates the type of error that is generated.</p>"""
    can_retry: "aws_sdk_inspector.types.bool.Bool"
    """<p>You can immediately retry your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_inspector.types.access_denied_error_code

    out["errorCode"] = (
        aws_sdk_inspector.types.access_denied_error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    )
    out["canRetry"] = value["can_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    if "errorCode" in data:
        import aws_sdk_inspector.types.access_denied_error_code

        out["error_code"] = (
            aws_sdk_inspector.types.access_denied_error_code.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError("AccessDeniedException_.error_code required")
    if "canRetry" in data:
        out["can_retry"] = data["canRetry"]
    else:
        raise DeserializationError("AccessDeniedException_.can_retry required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_1(data))
