"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#InternalServerException``."""

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError, ServiceError


class InternalServerException_(TypedDict, closed=True):
    message: "str"


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
    """Modeled error for Smithy shape ``com.amazonaws.redshiftserverless#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_1(data))
