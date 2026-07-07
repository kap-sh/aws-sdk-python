"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#InvalidEndpointRegionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.error_message


class InvalidEndpointRegionException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_marketplace_metering.types.error_message.errorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidEndpointRegionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidEndpointRegionException_:
    out: InvalidEndpointRegionException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidEndpointRegionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#InvalidEndpointRegionException``."""

    code: str | None = "InvalidEndpointRegionException"

    def __init__(self, data: InvalidEndpointRegionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidEndpointRegionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidEndpointRegionException":
        return cls(deserialize_aws_json_1_1(data))
