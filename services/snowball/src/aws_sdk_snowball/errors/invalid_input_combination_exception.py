"""Generated from Smithy shape ``com.amazonaws.snowball#InvalidInputCombinationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_snowball.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.string


class InvalidInputCombinationException_(TypedDict):
    message: NotRequired["aws_sdk_snowball.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInputCombinationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInputCombinationException_:
    out: InvalidInputCombinationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidInputCombinationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#InvalidInputCombinationException``."""

    code: str | None = "InvalidInputCombinationException"

    def __init__(self, data: InvalidInputCombinationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputCombinationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidInputCombinationException":
        return cls(deserialize_aws_json_1_1(data))
