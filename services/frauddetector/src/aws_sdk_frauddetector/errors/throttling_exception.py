"""Generated from Smithy shape ``com.amazonaws.frauddetector#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_frauddetector.types.string.string"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.frauddetector#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_1(data))
