"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#InvalidPaginationException``."""

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError, ServiceError


class InvalidPaginationException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPaginationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPaginationException_:
    out: InvalidPaginationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidPaginationException_.message required")
    return out


class InvalidPaginationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftserverless#InvalidPaginationException``."""

    code: str | None = "InvalidPaginationException"

    def __init__(self, data: InvalidPaginationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPaginationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPaginationException":
        return cls(deserialize_aws_json_1_1(data))
