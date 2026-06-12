"""Generated from Smithy shape ``com.amazonaws.glacier#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glacier.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class ResourceNotFoundException_(TypedDict):
    type: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Client</p>"""
    code: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>404 Not Found</p>"""
    message: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_json(data))
