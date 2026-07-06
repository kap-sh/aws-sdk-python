"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#InternalServiceErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.error_message


class InternalServiceErrorException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_marketplace_metering.types.error_message.errorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServiceErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServiceErrorException_:
    out: InternalServiceErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServiceErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#InternalServiceErrorException``."""

    code: str | None = "InternalServiceErrorException"

    def __init__(self, data: InternalServiceErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceErrorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServiceErrorException":
        return cls(deserialize_aws_json_1_1(data))
