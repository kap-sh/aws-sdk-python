"""Generated from Smithy shape ``com.amazonaws.simpledbv2#NoSuchExportException``."""

from typing_extensions import TypedDict

from capo_simpledbv2.errors import DeserializationError, ServiceError


class NoSuchExportException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: NoSuchExportException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NoSuchExportException_:
    out: NoSuchExportException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NoSuchExportException_.message required")
    return out


class NoSuchExportException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.simpledbv2#NoSuchExportException``."""

    code: str | None = "NoSuchExportException"

    def __init__(self, data: NoSuchExportException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchExportException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NoSuchExportException":
        return cls(deserialize_json(data))
