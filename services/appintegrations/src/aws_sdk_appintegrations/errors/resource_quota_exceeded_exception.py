"""Generated from Smithy shape ``com.amazonaws.appintegrations#ResourceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appintegrations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.message


class ResourceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appintegrations.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceQuotaExceededException_:
    out: ResourceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appintegrations#ResourceQuotaExceededException``."""

    code: str | None = "ResourceQuotaExceededException"

    def __init__(self, data: ResourceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceQuotaExceededException":
        return cls(deserialize_json(data))
