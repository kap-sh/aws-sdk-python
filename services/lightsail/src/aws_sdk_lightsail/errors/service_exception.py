"""Generated from Smithy shape ``com.amazonaws.lightsail#ServiceException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string


class ServiceException_(TypedDict):
    code: NotRequired["aws_sdk_lightsail.types.string.string"]
    docs: NotRequired["aws_sdk_lightsail.types.string.string"]
    message: NotRequired["aws_sdk_lightsail.types.string.string"]
    tip: NotRequired["aws_sdk_lightsail.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceException_) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ServiceException_:
    out: ServiceException_ = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "docs" in data:
        out["docs"] = data["docs"]
    if "message" in data:
        out["message"] = data["message"]
    if "tip" in data:
        out["tip"] = data["tip"]
    return out


class ServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lightsail#ServiceException``."""

    code: str | None = "ServiceException"

    def __init__(self, data: ServiceException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServiceException":
        return cls(deserialize_aws_json_1_1(data))
