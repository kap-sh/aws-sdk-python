"""Generated from Smithy shape ``com.amazonaws.odb#ThrottlingException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError, ServiceError


class ThrottlingException_(TypedDict):
    message: "str"
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying the request after being throttled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.odb#ThrottlingException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data))
