"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#OcuLimitExceededException``."""

from typing import TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError, ServiceError


class OcuLimitExceededException_(TypedDict):
    message: "str"
    """Description of the error."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OcuLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OcuLimitExceededException_:
    out: OcuLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("OcuLimitExceededException_.message required")
    return out


class OcuLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.opensearchserverless#OcuLimitExceededException``."""

    code: str | None = "OcuLimitExceededException"

    def __init__(self, data: OcuLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OcuLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "OcuLimitExceededException":
        return cls(deserialize_aws_json_1_0(data))
