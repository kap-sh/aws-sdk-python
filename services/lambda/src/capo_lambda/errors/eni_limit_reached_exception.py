"""Generated from Smithy shape ``com.amazonaws.lambda#ENILimitReachedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class ENILimitReachedException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    message: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ENILimitReachedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ENILimitReachedException_:
    out: ENILimitReachedException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ENILimitReachedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#ENILimitReachedException``."""

    code: str | None = "ENILimitReachedException"

    def __init__(self, data: ENILimitReachedException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ENILimitReachedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ENILimitReachedException":
        return cls(deserialize_json(data))
