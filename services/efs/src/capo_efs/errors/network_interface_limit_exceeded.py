"""Generated from Smithy shape ``com.amazonaws.efs#NetworkInterfaceLimitExceeded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class NetworkInterfaceLimitExceeded_(TypedDict, closed=True):
    error_code: "capo_efs.types.error_code.ErrorCode"
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaceLimitExceeded_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NetworkInterfaceLimitExceeded_:
    out: NetworkInterfaceLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("NetworkInterfaceLimitExceeded_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NetworkInterfaceLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#NetworkInterfaceLimitExceeded``."""

    code: str | None = "NetworkInterfaceLimitExceeded"

    def __init__(self, data: NetworkInterfaceLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NetworkInterfaceLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NetworkInterfaceLimitExceeded":
        return cls(deserialize_json(data))
