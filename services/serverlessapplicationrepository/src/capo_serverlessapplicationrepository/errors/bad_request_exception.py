"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#BadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_serverlessapplicationrepository.errors import ServiceError

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class BadRequestException_(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>400</p>"""
    message: NotRequired["capo_serverlessapplicationrepository.types.__string.__string"]
    """<p>One of the parameters in the request is invalid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.serverlessapplicationrepository#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(self, data: BadRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadRequestException":
        return cls(deserialize_json(data))
