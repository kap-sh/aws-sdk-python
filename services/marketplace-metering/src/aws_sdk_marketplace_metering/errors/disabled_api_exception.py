"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#DisabledApiException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.error_message


class DisabledApiException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_marketplace_metering.types.error_message.errorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisabledApiException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisabledApiException_:
    out: DisabledApiException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DisabledApiException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#DisabledApiException``."""

    code: str | None = "DisabledApiException"

    def __init__(self, data: DisabledApiException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DisabledApiException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DisabledApiException":
        return cls(deserialize_aws_json_1_1(data))
