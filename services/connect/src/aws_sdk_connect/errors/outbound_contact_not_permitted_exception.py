"""Generated from Smithy shape ``com.amazonaws.connect#OutboundContactNotPermittedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_connect.types.message


class OutboundContactNotPermittedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_connect.types.message.Message"]
    """<p>The message about the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundContactNotPermittedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> OutboundContactNotPermittedException_:
    out: OutboundContactNotPermittedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class OutboundContactNotPermittedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#OutboundContactNotPermittedException``."""

    code: str | None = "OutboundContactNotPermittedException"

    def __init__(self, data: OutboundContactNotPermittedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OutboundContactNotPermittedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "OutboundContactNotPermittedException":
        return cls(deserialize_json(data))
