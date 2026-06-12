"""Generated from Smithy shape ``com.amazonaws.glacier#RequestTimeoutException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glacier.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class RequestTimeoutException_(TypedDict):
    type: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Client</p>"""
    code: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>408 Request Timeout</p>"""
    message: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Returned if, when uploading an archive, Amazon Glacier times out while receiving the upload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestTimeoutException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestTimeoutException_:
    out: RequestTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RequestTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#RequestTimeoutException``."""

    code: str | None = "RequestTimeoutException"

    def __init__(self, data: RequestTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RequestTimeoutException":
        return cls(deserialize_json(data))
