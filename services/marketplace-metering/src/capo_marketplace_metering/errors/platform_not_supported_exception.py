"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#PlatformNotSupportedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_metering.types.error_message


class PlatformNotSupportedException_(TypedDict, closed=True):
    message: NotRequired["capo_marketplace_metering.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformNotSupportedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlatformNotSupportedException_:
    out: PlatformNotSupportedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PlatformNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#PlatformNotSupportedException``."""

    code: str | None = "PlatformNotSupportedException"

    def __init__(self, data: PlatformNotSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PlatformNotSupportedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PlatformNotSupportedException":
        return cls(deserialize_aws_json_1_1(data))
