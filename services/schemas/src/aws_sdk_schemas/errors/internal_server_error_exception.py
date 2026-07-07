"""Generated from Smithy shape ``com.amazonaws.schemas#InternalServerErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_schemas.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class InternalServerErrorException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The message string of the error output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.schemas#InternalServerErrorException``."""

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
