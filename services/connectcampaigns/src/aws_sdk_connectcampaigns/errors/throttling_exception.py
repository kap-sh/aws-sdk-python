"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.x_amazon_error_type


class ThrottlingException_(TypedDict, closed=True):
    message: "str"
    x_amz_error_type: NotRequired[
        "aws_sdk_connectcampaigns.types.x_amazon_error_type.XAmazonErrorType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectcampaigns#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
