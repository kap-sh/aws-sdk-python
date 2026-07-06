"""Generated from Smithy shape ``com.amazonaws.guardduty#InternalServerErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_guardduty.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class InternalServerErrorException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The error message.</p>"""
    type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The error type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "type" in data:
        out["type"] = data["type"]
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.guardduty#InternalServerErrorException``."""

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
