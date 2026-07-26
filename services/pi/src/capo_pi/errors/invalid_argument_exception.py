"""Generated from Smithy shape ``com.amazonaws.pi#InvalidArgumentException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pi.errors import ServiceError

if TYPE_CHECKING:
    import capo_pi.types.error_string


class InvalidArgumentException_(TypedDict, closed=True):
    message: NotRequired["capo_pi.types.error_string.ErrorString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidArgumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidArgumentException_:
    out: InvalidArgumentException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pi#InvalidArgumentException``."""

    code: str | None = "InvalidArgumentException"

    def __init__(self, data: InvalidArgumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArgumentException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidArgumentException":
        return cls(deserialize_aws_json_1_1(data))
