"""Generated from Smithy shape ``com.amazonaws.lambda#PolicyLengthExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class PolicyLengthExceededException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    message: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyLengthExceededException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicyLengthExceededException_:
    out: PolicyLengthExceededException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PolicyLengthExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#PolicyLengthExceededException``."""

    code: str | None = "PolicyLengthExceededException"

    def __init__(self, data: PolicyLengthExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyLengthExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PolicyLengthExceededException":
        return cls(deserialize_json(data))
