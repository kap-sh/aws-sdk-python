"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DryRunOperationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.error_message


class DryRunOperationException_(TypedDict):
    message: NotRequired["aws_sdk_imagebuilder.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DryRunOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DryRunOperationException_:
    out: DryRunOperationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DryRunOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.imagebuilder#DryRunOperationException``."""

    code: str | None = "DryRunOperationException"

    def __init__(self, data: DryRunOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DryRunOperationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DryRunOperationException":
        return cls(deserialize_json(data))
