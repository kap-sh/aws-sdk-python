"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceServiceQuotaExceededException``."""

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, ServiceError


class RouterNetworkInterfaceServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(
    data: dict,
) -> RouterNetworkInterfaceServiceQuotaExceededException_:
    out: RouterNetworkInterfaceServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "RouterNetworkInterfaceServiceQuotaExceededException_.message required"
        )
    return out


class RouterNetworkInterfaceServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceServiceQuotaExceededException``."""

    code: str | None = "RouterNetworkInterfaceServiceQuotaExceededException"

    def __init__(self, data: RouterNetworkInterfaceServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RouterNetworkInterfaceServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict
    ) -> "RouterNetworkInterfaceServiceQuotaExceededException":
        return cls(deserialize_json(data))
