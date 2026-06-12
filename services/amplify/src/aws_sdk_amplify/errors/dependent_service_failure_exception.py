"""Generated from Smithy shape ``com.amazonaws.amplify#DependentServiceFailureException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplify.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.error_message


class DependentServiceFailureException_(TypedDict):
    message: NotRequired["aws_sdk_amplify.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DependentServiceFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependentServiceFailureException_:
    out: DependentServiceFailureException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DependentServiceFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.amplify#DependentServiceFailureException``."""

    code: str | None = "DependentServiceFailureException"

    def __init__(self, data: DependentServiceFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DependentServiceFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DependentServiceFailureException":
        return cls(deserialize_json(data))
