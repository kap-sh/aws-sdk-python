"""Generated from Smithy shape ``com.amazonaws.devicefarm#ArgumentException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.message


class ArgumentException_(TypedDict):
    message: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>Any additional information about the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArgumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ArgumentException_:
    out: ArgumentException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devicefarm#ArgumentException``."""

    code: str | None = "ArgumentException"

    def __init__(self, data: ArgumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ArgumentException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ArgumentException":
        return cls(deserialize_aws_json_1_1(data))
