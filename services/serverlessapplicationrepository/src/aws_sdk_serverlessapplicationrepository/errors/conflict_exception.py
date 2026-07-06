"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_serverlessapplicationrepository.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string


class ConflictException_(TypedDict, closed=True):
    error_code: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>409</p>"""
    message: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The resource already exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.serverlessapplicationrepository#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
