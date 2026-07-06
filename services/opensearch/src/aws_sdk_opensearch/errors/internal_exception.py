"""Generated from Smithy shape ``com.amazonaws.opensearch#InternalException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearch.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.error_message


class InternalException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_opensearch.types.error_message.ErrorMessage"]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalException_:
    out: InternalException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.opensearch#InternalException``."""

    code: str | None = "InternalException"

    def __init__(self, data: InternalException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalException":
        return cls(deserialize_json(data))
