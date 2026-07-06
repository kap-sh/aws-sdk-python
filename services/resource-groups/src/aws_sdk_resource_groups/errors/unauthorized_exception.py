"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UnauthorizedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resource_groups.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.error_message


class UnauthorizedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_resource_groups.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedException_:
    out: UnauthorizedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnauthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.resourcegroups#UnauthorizedException``."""

    code: str | None = "UnauthorizedException"

    def __init__(self, data: UnauthorizedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnauthorizedException":
        return cls(deserialize_json(data))
