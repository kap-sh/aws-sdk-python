"""Generated from Smithy shape ``com.amazonaws.gamelift#UnsupportedRegionException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_empty_string


class UnsupportedRegionException_(TypedDict):
    message: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedRegionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedRegionException_:
    out: UnsupportedRegionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedRegionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#UnsupportedRegionException``."""

    code: str | None = "UnsupportedRegionException"

    def __init__(self, data: UnsupportedRegionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedRegionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedRegionException":
        return cls(deserialize_aws_json_1_1(data))
