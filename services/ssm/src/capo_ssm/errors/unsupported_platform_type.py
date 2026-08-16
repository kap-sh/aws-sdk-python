"""Generated from Smithy shape ``com.amazonaws.ssm#UnsupportedPlatformType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class UnsupportedPlatformType_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedPlatformType_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedPlatformType_:
    out: UnsupportedPlatformType_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedPlatformType(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#UnsupportedPlatformType``."""

    code: str | None = "UnsupportedPlatformType"

    def __init__(self, data: UnsupportedPlatformType_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedPlatformType",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "UnsupportedPlatformType":
        return cls(deserialize_aws_json_1_1(data), message)
