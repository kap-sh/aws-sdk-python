"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.retry_after_seconds
    import aws_sdk_iotfleetwise.types.string


class InternalServerException_(TypedDict, closed=True):
    message: "aws_sdk_iotfleetwise.types.string.string"
    retry_after_seconds: (
        "aws_sdk_iotfleetwise.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>The number of seconds to wait before retrying the command.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_0(data))
