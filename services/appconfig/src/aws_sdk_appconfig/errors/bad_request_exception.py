"""Generated from Smithy shape ``com.amazonaws.appconfig#BadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appconfig.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.bad_request_details
    import aws_sdk_appconfig.types.bad_request_reason
    import aws_sdk_appconfig.types.string


class BadRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appconfig.types.string.String"]
    reason: NotRequired["aws_sdk_appconfig.types.bad_request_reason.BadRequestReason"]
    details: NotRequired[
        "aws_sdk_appconfig.types.bad_request_details.BadRequestDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_appconfig.types.bad_request_reason

        out["Reason"] = aws_sdk_appconfig.types.bad_request_reason.serialize_json(
            value["reason"]
        )
    if "details" in value:
        import aws_sdk_appconfig.types.bad_request_details

        out["Details"] = aws_sdk_appconfig.types.bad_request_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_appconfig.types.bad_request_reason

        out["reason"] = aws_sdk_appconfig.types.bad_request_reason.deserialize_json(
            data["Reason"]
        )
    if "Details" in data:
        import aws_sdk_appconfig.types.bad_request_details

        out["details"] = aws_sdk_appconfig.types.bad_request_details.deserialize_json(
            data["Details"]
        )
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appconfig#BadRequestException``."""

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
