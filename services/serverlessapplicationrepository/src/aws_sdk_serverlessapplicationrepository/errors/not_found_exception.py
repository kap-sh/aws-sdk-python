"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#NotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_serverlessapplicationrepository.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string


class NotFoundException_(TypedDict, closed=True):
    error_code: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>404</p>"""
    message: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundException_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.serverlessapplicationrepository#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(self, data: NotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotFoundException":
        return cls(deserialize_json(data))
