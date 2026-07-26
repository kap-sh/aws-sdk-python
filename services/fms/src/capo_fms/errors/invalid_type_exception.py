"""Generated from Smithy shape ``com.amazonaws.fms#InvalidTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import ServiceError

if TYPE_CHECKING:
    import capo_fms.types.error_message


class InvalidTypeException_(TypedDict, closed=True):
    message: NotRequired["capo_fms.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidTypeException_:
    out: InvalidTypeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fms#InvalidTypeException``."""

    code: str | None = "InvalidTypeException"

    def __init__(self, data: InvalidTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidTypeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidTypeException":
        return cls(deserialize_aws_json_1_1(data))
