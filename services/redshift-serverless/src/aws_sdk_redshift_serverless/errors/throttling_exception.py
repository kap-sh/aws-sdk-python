"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ThrottlingException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift_serverless.errors import ServiceError


class ThrottlingException_(TypedDict):
    code: NotRequired["str"]
    message: NotRequired["str"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftserverless#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_1(data))
