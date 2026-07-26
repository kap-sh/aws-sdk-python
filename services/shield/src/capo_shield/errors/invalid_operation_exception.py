"""Generated from Smithy shape ``com.amazonaws.shield#InvalidOperationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_shield.errors import ServiceError

if TYPE_CHECKING:
    import capo_shield.types.error_message


class InvalidOperationException_(TypedDict, closed=True):
    message: NotRequired["capo_shield.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidOperationException_:
    out: InvalidOperationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#InvalidOperationException``."""

    code: str | None = "InvalidOperationException"

    def __init__(self, data: InvalidOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidOperationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidOperationException":
        return cls(deserialize_aws_json_1_1(data))
