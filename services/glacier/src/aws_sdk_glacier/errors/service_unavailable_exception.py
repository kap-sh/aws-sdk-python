"""Generated from Smithy shape ``com.amazonaws.glacier#ServiceUnavailableException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glacier.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class ServiceUnavailableException_(TypedDict):
    type: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Server</p>"""
    code: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>500 Internal Server Error</p>"""
    message: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Returned if the service cannot complete the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceUnavailableException_:
    out: ServiceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#ServiceUnavailableException``."""

    code: str | None = "ServiceUnavailableException"

    def __init__(self, data: ServiceUnavailableException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceUnavailableException":
        return cls(deserialize_json(data))
