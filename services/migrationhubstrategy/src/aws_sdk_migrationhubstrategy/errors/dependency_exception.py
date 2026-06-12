"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#DependencyException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhubstrategy.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.error_message


class DependencyException_(TypedDict):
    message: NotRequired[
        "aws_sdk_migrationhubstrategy.types.error_message.errorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependencyException_:
    out: DependencyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubstrategy#DependencyException``."""

    code: str | None = "DependencyException"

    def __init__(self, data: DependencyException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DependencyException":
        return cls(deserialize_json(data))
