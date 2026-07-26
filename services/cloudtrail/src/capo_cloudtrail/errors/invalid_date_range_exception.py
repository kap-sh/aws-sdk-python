"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InvalidDateRangeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudtrail.types.error_message


class InvalidDateRangeException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidDateRangeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidDateRangeException_:
    out: InvalidDateRangeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidDateRangeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InvalidDateRangeException``."""

    code: str | None = "InvalidDateRangeException"

    def __init__(self, data: InvalidDateRangeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDateRangeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidDateRangeException":
        return cls(deserialize_aws_json_1_1(data))
