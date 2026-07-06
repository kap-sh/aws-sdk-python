"""Generated from Smithy shape ``com.amazonaws.ssm#UnsupportedParameterType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class UnsupportedParameterType_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedParameterType_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedParameterType_:
    out: UnsupportedParameterType_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedParameterType(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#UnsupportedParameterType``."""

    code: str | None = "UnsupportedParameterType"

    def __init__(self, data: UnsupportedParameterType_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedParameterType",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedParameterType":
        return cls(deserialize_aws_json_1_1(data))
