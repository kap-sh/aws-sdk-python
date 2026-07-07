"""Generated from Smithy shape ``com.amazonaws.frauddetector#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string


class InternalServerException_(TypedDict, closed=True):
    message: "aws_sdk_frauddetector.types.string.string"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.frauddetector#InternalServerException``."""

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
    def from_aws_json_1_1(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_1(data))
