"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#InvalidEncodingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehendmedical.errors import ServiceError

if TYPE_CHECKING:
    import capo_comprehendmedical.types.string


class InvalidEncodingException_(TypedDict, closed=True):
    message: NotRequired["capo_comprehendmedical.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidEncodingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidEncodingException_:
    out: InvalidEncodingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidEncodingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.comprehendmedical#InvalidEncodingException``."""

    code: str | None = "InvalidEncodingException"

    def __init__(self, data: InvalidEncodingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidEncodingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidEncodingException":
        return cls(deserialize_aws_json_1_1(data))
