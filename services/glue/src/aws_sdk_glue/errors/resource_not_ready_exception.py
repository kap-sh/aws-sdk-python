"""Generated from Smithy shape ``com.amazonaws.glue#ResourceNotReadyException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class ResourceNotReadyException_(TypedDict):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotReadyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotReadyException_:
    out: ResourceNotReadyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceNotReadyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#ResourceNotReadyException``."""

    code: str | None = "ResourceNotReadyException"

    def __init__(self, data: ResourceNotReadyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotReadyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceNotReadyException":
        return cls(deserialize_aws_json_1_1(data))
