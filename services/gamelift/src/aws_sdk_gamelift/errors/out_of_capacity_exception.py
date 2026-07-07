"""Generated from Smithy shape ``com.amazonaws.gamelift#OutOfCapacityException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_empty_string


class OutOfCapacityException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutOfCapacityException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutOfCapacityException_:
    out: OutOfCapacityException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class OutOfCapacityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#OutOfCapacityException``."""

    code: str | None = "OutOfCapacityException"

    def __init__(self, data: OutOfCapacityException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OutOfCapacityException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OutOfCapacityException":
        return cls(deserialize_aws_json_1_1(data))
