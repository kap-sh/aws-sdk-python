"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DryRunException``."""

from typing_extensions import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError, ServiceError


class DryRunException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DryRunException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DryRunException_:
    out: DryRunException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DryRunException_.message required")
    return out


class DryRunException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftserverless#DryRunException``."""

    code: str | None = "DryRunException"

    def __init__(self, data: DryRunException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DryRunException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DryRunException":
        return cls(deserialize_aws_json_1_1(data))
