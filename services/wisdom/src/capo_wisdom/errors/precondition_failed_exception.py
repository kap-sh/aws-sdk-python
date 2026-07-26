"""Generated from Smithy shape ``com.amazonaws.wisdom#PreconditionFailedException``."""

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import ServiceError


class PreconditionFailedException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: PreconditionFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PreconditionFailedException_:
    out: PreconditionFailedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PreconditionFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wisdom#PreconditionFailedException``."""

    code: str | None = "PreconditionFailedException"

    def __init__(self, data: PreconditionFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PreconditionFailedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PreconditionFailedException":
        return cls(deserialize_json(data))
