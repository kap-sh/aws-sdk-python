"""Generated from Smithy shape ``com.amazonaws.shield#InvalidResourceException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_shield.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_shield.types.error_message


class InvalidResourceException_(TypedDict):
    message: NotRequired["aws_sdk_shield.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidResourceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidResourceException_:
    out: InvalidResourceException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#InvalidResourceException``."""

    code: str | None = "InvalidResourceException"

    def __init__(self, data: InvalidResourceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidResourceException":
        return cls(deserialize_aws_json_1_1(data))
