"""Generated from Smithy shape ``com.amazonaws.kinesis#KMSOptInRequired``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.error_message


class KMSOptInRequired_(TypedDict):
    message: NotRequired["aws_sdk_kinesis.types.error_message.ErrorMessage"]
    """<p>A message that provides information about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSOptInRequired_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSOptInRequired_:
    out: KMSOptInRequired_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KMSOptInRequired(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesis#KMSOptInRequired``."""

    code: str | None = "KMSOptInRequired"

    def __init__(self, data: KMSOptInRequired_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSOptInRequired",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KMSOptInRequired":
        return cls(deserialize_aws_json_1_1(data))
