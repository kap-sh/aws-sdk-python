"""Generated from Smithy shape ``com.amazonaws.snowball#InvalidAddressException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_snowball.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.string


class InvalidAddressException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_snowball.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidAddressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidAddressException_:
    out: InvalidAddressException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidAddressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#InvalidAddressException``."""

    code: str | None = "InvalidAddressException"

    def __init__(self, data: InvalidAddressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAddressException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidAddressException":
        return cls(deserialize_aws_json_1_1(data))
