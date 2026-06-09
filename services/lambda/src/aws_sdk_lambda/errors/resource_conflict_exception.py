"""Generated from Smithy shape ``com.amazonaws.lambda#ResourceConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class ResourceConflictException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConflictException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceConflictException_:
    out: ResourceConflictException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#ResourceConflictException``."""

    code: str | None = "ResourceConflictException"

    def __init__(self, data: ResourceConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceConflictException":
        return cls(deserialize_json(data))
