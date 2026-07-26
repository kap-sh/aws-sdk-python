"""Generated from Smithy shape ``com.amazonaws.acm#InvalidStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm.errors import ServiceError

if TYPE_CHECKING:
    import capo_acm.types.string


class InvalidStateException_(TypedDict, closed=True):
    message: NotRequired["capo_acm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidStateException_:
    out: InvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acm#InvalidStateException``."""

    code: str | None = "InvalidStateException"

    def __init__(self, data: InvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidStateException":
        return cls(deserialize_aws_json_1_1(data))
