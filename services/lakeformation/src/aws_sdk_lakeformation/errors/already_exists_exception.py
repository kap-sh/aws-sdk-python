"""Generated from Smithy shape ``com.amazonaws.lakeformation#AlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.message_string


class AlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AlreadyExistsException_:
    out: AlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#AlreadyExistsException``."""

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
    def from_json(cls, data: dict) -> "AlreadyExistsException":
        return cls(deserialize_json(data))
