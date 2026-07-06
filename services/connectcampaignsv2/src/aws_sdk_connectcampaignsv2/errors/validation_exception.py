"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.x_amazon_error_type


class ValidationException_(TypedDict, closed=True):
    message: "str"
    x_amz_error_type: NotRequired[
        "aws_sdk_connectcampaignsv2.types.x_amazon_error_type.XAmazonErrorType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectcampaignsv2#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ValidationException":
        return cls(deserialize_json(data))
