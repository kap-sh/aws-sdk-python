"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#DuplicateRequestException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.error_message


class DuplicateRequestException_(TypedDict):
    message: NotRequired[
        "aws_sdk_marketplace_metering.types.error_message.errorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateRequestException_:
    out: DuplicateRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DuplicateRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#DuplicateRequestException``."""

    code: str | None = "DuplicateRequestException"

    def __init__(self, data: DuplicateRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateRequestException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DuplicateRequestException":
        return cls(deserialize_aws_json_1_1(data))
