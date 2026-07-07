"""Generated from Smithy shape ``com.amazonaws.comprehend#InvalidRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_comprehend.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.invalid_request_detail
    import aws_sdk_comprehend.types.invalid_request_reason
    import aws_sdk_comprehend.types.string


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_comprehend.types.string.String"]
    reason: NotRequired[
        "aws_sdk_comprehend.types.invalid_request_reason.InvalidRequestReason"
    ]
    detail: NotRequired[
        "aws_sdk_comprehend.types.invalid_request_detail.InvalidRequestDetail"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_comprehend.types.invalid_request_reason

        out["Reason"] = (
            aws_sdk_comprehend.types.invalid_request_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    if "detail" in value:
        import aws_sdk_comprehend.types.invalid_request_detail

        out["Detail"] = (
            aws_sdk_comprehend.types.invalid_request_detail.serialize_aws_json_1_1(
                value["detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_comprehend.types.invalid_request_reason

        out["reason"] = (
            aws_sdk_comprehend.types.invalid_request_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    if "Detail" in data:
        import aws_sdk_comprehend.types.invalid_request_detail

        out["detail"] = (
            aws_sdk_comprehend.types.invalid_request_detail.deserialize_aws_json_1_1(
                data["Detail"]
            )
        )
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.comprehend#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidRequestException":
        return cls(deserialize_aws_json_1_1(data))
