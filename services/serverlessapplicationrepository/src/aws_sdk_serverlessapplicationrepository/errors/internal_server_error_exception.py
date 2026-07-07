"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#InternalServerErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_serverlessapplicationrepository.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string


class InternalServerErrorException_(TypedDict, closed=True):
    error_code: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>500</p>"""
    message: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The AWS Serverless Application Repository service encountered an internal error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.serverlessapplicationrepository#InternalServerErrorException``."""

    code: str | None = "InternalServerErrorException"

    def __init__(self, data: InternalServerErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerErrorException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerErrorException":
        return cls(deserialize_json(data))
