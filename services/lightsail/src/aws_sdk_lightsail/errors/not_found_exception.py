"""Generated from Smithy shape ``com.amazonaws.lightsail#NotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string


class NotFoundException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_lightsail.types.string.string"]
    docs: NotRequired["aws_sdk_lightsail.types.string.string"]
    message: NotRequired["aws_sdk_lightsail.types.string.string"]
    tip: NotRequired["aws_sdk_lightsail.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotFoundException_) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "docs" in data:
        out["docs"] = data["docs"]
    if "message" in data:
        out["message"] = data["message"]
    if "tip" in data:
        out["tip"] = data["tip"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lightsail#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(self, data: NotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NotFoundException":
        return cls(deserialize_aws_json_1_1(data))
