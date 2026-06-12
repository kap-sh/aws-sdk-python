"""Generated from Smithy shape ``com.amazonaws.lakeformation#ExpiredException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.message_string


class ExpiredException_(TypedDict):
    message: NotRequired["aws_sdk_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ExpiredException_:
    out: ExpiredException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ExpiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#ExpiredException``."""

    code: str | None = "ExpiredException"

    def __init__(self, data: ExpiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExpiredException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ExpiredException":
        return cls(deserialize_json(data))
