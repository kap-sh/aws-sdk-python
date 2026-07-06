"""Generated from Smithy shape ``com.amazonaws.glue#ConcurrentRunsExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class ConcurrentRunsExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConcurrentRunsExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConcurrentRunsExceededException_:
    out: ConcurrentRunsExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ConcurrentRunsExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#ConcurrentRunsExceededException``."""

    code: str | None = "ConcurrentRunsExceededException"

    def __init__(self, data: ConcurrentRunsExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentRunsExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ConcurrentRunsExceededException":
        return cls(deserialize_aws_json_1_1(data))
