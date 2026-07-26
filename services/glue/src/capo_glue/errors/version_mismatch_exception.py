"""Generated from Smithy shape ``com.amazonaws.glue#VersionMismatchException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.message_string


class VersionMismatchException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VersionMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VersionMismatchException_:
    out: VersionMismatchException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class VersionMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#VersionMismatchException``."""

    code: str | None = "VersionMismatchException"

    def __init__(self, data: VersionMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="VersionMismatchException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "VersionMismatchException":
        return cls(deserialize_aws_json_1_1(data))
