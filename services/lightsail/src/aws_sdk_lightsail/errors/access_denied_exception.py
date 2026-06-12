"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string


class AccessDeniedException_(TypedDict):
    code: NotRequired["aws_sdk_lightsail.types.string.string"]
    docs: NotRequired["aws_sdk_lightsail.types.string.string"]
    message: NotRequired["aws_sdk_lightsail.types.string.string"]
    tip: NotRequired["aws_sdk_lightsail.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "docs" in value:
        out["docs"] = value["docs"]
    if "message" in value:
        out["message"] = value["message"]
    if "tip" in value:
        out["tip"] = value["tip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "docs" in data:
        out["docs"] = data["docs"]
    if "message" in data:
        out["message"] = data["message"]
    if "tip" in data:
        out["tip"] = data["tip"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lightsail#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_1(data))
