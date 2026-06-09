"""Generated from Smithy shape ``com.amazonaws.lambda#EC2UnexpectedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class EC2UnexpectedException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]
    ec2_error_code: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: EC2UnexpectedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    if "ec2_error_code" in value:
        out["EC2ErrorCode"] = value["ec2_error_code"]
    return out


def deserialize_json(data: dict) -> EC2UnexpectedException_:
    out: EC2UnexpectedException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "EC2ErrorCode" in data:
        out["ec2_error_code"] = data["EC2ErrorCode"]
    return out


class EC2UnexpectedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#EC2UnexpectedException``."""

    code: str | None = "EC2UnexpectedException"

    def __init__(self, data: EC2UnexpectedException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="EC2UnexpectedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "EC2UnexpectedException":
        return cls(deserialize_json(data))
