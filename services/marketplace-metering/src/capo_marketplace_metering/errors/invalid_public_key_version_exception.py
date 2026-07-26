"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#InvalidPublicKeyVersionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_metering.types.error_message


class InvalidPublicKeyVersionException_(TypedDict, closed=True):
    message: NotRequired["capo_marketplace_metering.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPublicKeyVersionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPublicKeyVersionException_:
    out: InvalidPublicKeyVersionException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidPublicKeyVersionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#InvalidPublicKeyVersionException``."""

    code: str | None = "InvalidPublicKeyVersionException"

    def __init__(self, data: InvalidPublicKeyVersionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPublicKeyVersionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPublicKeyVersionException":
        return cls(deserialize_aws_json_1_1(data))
