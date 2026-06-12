"""Generated from Smithy shape ``com.amazonaws.gamelift#TaggingFailedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_empty_string


class TaggingFailedException_(TypedDict):
    message: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaggingFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TaggingFailedException_:
    out: TaggingFailedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TaggingFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#TaggingFailedException``."""

    code: str | None = "TaggingFailedException"

    def __init__(self, data: TaggingFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TaggingFailedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TaggingFailedException":
        return cls(deserialize_aws_json_1_1(data))
