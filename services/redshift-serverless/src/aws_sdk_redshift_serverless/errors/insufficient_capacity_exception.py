"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#InsufficientCapacityException``."""

from typing_extensions import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError, ServiceError


class InsufficientCapacityException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsufficientCapacityException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InsufficientCapacityException_:
    out: InsufficientCapacityException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InsufficientCapacityException_.message required")
    return out


class InsufficientCapacityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftserverless#InsufficientCapacityException``."""

    code: str | None = "InsufficientCapacityException"

    def __init__(self, data: InsufficientCapacityException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="InsufficientCapacityException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InsufficientCapacityException":
        return cls(deserialize_aws_json_1_1(data))
