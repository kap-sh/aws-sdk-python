"""Generated from Smithy shape ``com.amazonaws.ssm#UnsupportedFeatureRequiredException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class UnsupportedFeatureRequiredException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedFeatureRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedFeatureRequiredException_:
    out: UnsupportedFeatureRequiredException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedFeatureRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#UnsupportedFeatureRequiredException``."""

    code: str | None = "UnsupportedFeatureRequiredException"

    def __init__(self, data: UnsupportedFeatureRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedFeatureRequiredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedFeatureRequiredException":
        return cls(deserialize_aws_json_1_1(data))
