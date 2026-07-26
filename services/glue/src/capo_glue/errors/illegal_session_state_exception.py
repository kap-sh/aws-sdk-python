"""Generated from Smithy shape ``com.amazonaws.glue#IllegalSessionStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.message_string


class IllegalSessionStateException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IllegalSessionStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IllegalSessionStateException_:
    out: IllegalSessionStateException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IllegalSessionStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#IllegalSessionStateException``."""

    code: str | None = "IllegalSessionStateException"

    def __init__(self, data: IllegalSessionStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalSessionStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IllegalSessionStateException":
        return cls(deserialize_aws_json_1_1(data))
