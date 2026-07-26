"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#InvalidContentLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmailmessageflow.errors import ServiceError

if TYPE_CHECKING:
    import capo_workmailmessageflow.types.error_message


class InvalidContentLocation_(TypedDict, closed=True):
    message: NotRequired["capo_workmailmessageflow.types.error_message.errorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidContentLocation_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidContentLocation_:
    out: InvalidContentLocation_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidContentLocation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmailmessageflow#InvalidContentLocation``."""

    code: str | None = "InvalidContentLocation"

    def __init__(self, data: InvalidContentLocation_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidContentLocation",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidContentLocation":
        return cls(deserialize_json(data))
