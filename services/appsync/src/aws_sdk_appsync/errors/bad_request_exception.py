"""Generated from Smithy shape ``com.amazonaws.appsync#BadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appsync.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.bad_request_detail
    import aws_sdk_appsync.types.bad_request_reason
    import aws_sdk_appsync.types.error_message


class BadRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appsync.types.error_message.ErrorMessage"]
    reason: NotRequired["aws_sdk_appsync.types.bad_request_reason.BadRequestReason"]
    detail: NotRequired["aws_sdk_appsync.types.bad_request_detail.BadRequestDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import aws_sdk_appsync.types.bad_request_reason

        out["reason"] = aws_sdk_appsync.types.bad_request_reason.serialize_json(
            value["reason"]
        )
    if "detail" in value:
        import aws_sdk_appsync.types.bad_request_detail

        out["detail"] = aws_sdk_appsync.types.bad_request_detail.serialize_json(
            value["detail"]
        )
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "reason" in data:
        import aws_sdk_appsync.types.bad_request_reason

        out["reason"] = aws_sdk_appsync.types.bad_request_reason.deserialize_json(
            data["reason"]
        )
    if "detail" in data:
        import aws_sdk_appsync.types.bad_request_detail

        out["detail"] = aws_sdk_appsync.types.bad_request_detail.deserialize_json(
            data["detail"]
        )
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appsync#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(self, data: BadRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadRequestException":
        return cls(deserialize_json(data))
