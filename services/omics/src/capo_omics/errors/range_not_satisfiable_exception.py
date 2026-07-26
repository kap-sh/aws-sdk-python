"""Generated from Smithy shape ``com.amazonaws.omics#RangeNotSatisfiableException``."""

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, ServiceError


class RangeNotSatisfiableException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RangeNotSatisfiableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RangeNotSatisfiableException_:
    out: RangeNotSatisfiableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("RangeNotSatisfiableException_.message required")
    return out


class RangeNotSatisfiableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.omics#RangeNotSatisfiableException``."""

    code: str | None = "RangeNotSatisfiableException"

    def __init__(self, data: RangeNotSatisfiableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="RangeNotSatisfiableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RangeNotSatisfiableException":
        return cls(deserialize_json(data))
