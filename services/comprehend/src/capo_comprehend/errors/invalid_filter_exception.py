"""Generated from Smithy shape ``com.amazonaws.comprehend#InvalidFilterException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import ServiceError

if TYPE_CHECKING:
    import capo_comprehend.types.string


class InvalidFilterException_(TypedDict, closed=True):
    message: NotRequired["capo_comprehend.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFilterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFilterException_:
    out: InvalidFilterException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidFilterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.comprehend#InvalidFilterException``."""

    code: str | None = "InvalidFilterException"

    def __init__(self, data: InvalidFilterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFilterException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidFilterException":
        return cls(deserialize_aws_json_1_1(data))
