"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#InvalidCampaignStateException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcampaignsv2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_state
    import aws_sdk_connectcampaignsv2.types.x_amazon_error_type


class InvalidCampaignStateException_(TypedDict):
    state: "aws_sdk_connectcampaignsv2.types.campaign_state.CampaignState"
    message: "str"
    x_amz_error_type: NotRequired[
        "aws_sdk_connectcampaignsv2.types.x_amazon_error_type.XAmazonErrorType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidCampaignStateException_) -> dict:
    out: dict = {}
    out["state"] = value["state"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidCampaignStateException_:
    out: InvalidCampaignStateException_ = {}  # type: ignore[typeddict-item]
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("InvalidCampaignStateException_.state required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidCampaignStateException_.message required")
    return out


class InvalidCampaignStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectcampaignsv2#InvalidCampaignStateException``."""

    code: str | None = "InvalidCampaignStateException"

    def __init__(self, data: InvalidCampaignStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCampaignStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidCampaignStateException":
        return cls(deserialize_json(data))
