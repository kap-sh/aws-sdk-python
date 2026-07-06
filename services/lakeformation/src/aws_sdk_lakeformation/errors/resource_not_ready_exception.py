"""Generated from Smithy shape ``com.amazonaws.lakeformation#ResourceNotReadyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.message_string


class ResourceNotReadyException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotReadyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotReadyException_:
    out: ResourceNotReadyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceNotReadyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#ResourceNotReadyException``."""

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
    def from_json(cls, data: dict) -> "ResourceNotReadyException":
        return cls(deserialize_json(data))
