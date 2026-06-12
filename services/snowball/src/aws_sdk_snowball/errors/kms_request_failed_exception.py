"""Generated from Smithy shape ``com.amazonaws.snowball#KMSRequestFailedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_snowball.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.string


class KMSRequestFailedException_(TypedDict):
    message: NotRequired["aws_sdk_snowball.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSRequestFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSRequestFailedException_:
    out: KMSRequestFailedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class KMSRequestFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#KMSRequestFailedException``."""

    code: str | None = "KMSRequestFailedException"

    def __init__(self, data: KMSRequestFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSRequestFailedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KMSRequestFailedException":
        return cls(deserialize_aws_json_1_1(data))
