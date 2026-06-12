"""Generated from Smithy shape ``com.amazonaws.shield#AccessDeniedForDependencyException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_shield.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_shield.types.error_message


class AccessDeniedForDependencyException_(TypedDict):
    message: NotRequired["aws_sdk_shield.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedForDependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessDeniedForDependencyException_:
    out: AccessDeniedForDependencyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AccessDeniedForDependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#AccessDeniedForDependencyException``."""

    code: str | None = "AccessDeniedForDependencyException"

    def __init__(self, data: AccessDeniedForDependencyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedForDependencyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccessDeniedForDependencyException":
        return cls(deserialize_aws_json_1_1(data))
