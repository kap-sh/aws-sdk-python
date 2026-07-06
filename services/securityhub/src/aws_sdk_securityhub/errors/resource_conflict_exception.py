"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityhub.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class ResourceConflictException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    code: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ResourceConflictException_:
    out: ResourceConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    return out


class ResourceConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securityhub#ResourceConflictException``."""

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
