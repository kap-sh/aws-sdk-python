"""Generated from Smithy shape ``com.amazonaws.glue#NoScheduleException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class NoScheduleException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoScheduleException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoScheduleException_:
    out: NoScheduleException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NoScheduleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#NoScheduleException``."""

    code: str | None = "NoScheduleException"

    def __init__(self, data: NoScheduleException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoScheduleException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NoScheduleException":
        return cls(deserialize_aws_json_1_1(data))
