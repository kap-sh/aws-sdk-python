"""Generated from Smithy shape ``com.amazonaws.glue#AlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class AlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AlreadyExistsException_:
    out: AlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#AlreadyExistsException``."""

    code: str | None = "AlreadyExistsException"

    def __init__(self, data: AlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
