"""Generated from Smithy shape ``com.amazonaws.gamelift#InvalidFleetStatusException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_empty_string


class InvalidFleetStatusException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFleetStatusException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFleetStatusException_:
    out: InvalidFleetStatusException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidFleetStatusException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#InvalidFleetStatusException``."""

    code: str | None = "InvalidFleetStatusException"

    def __init__(self, data: InvalidFleetStatusException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFleetStatusException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidFleetStatusException":
        return cls(deserialize_aws_json_1_1(data))
