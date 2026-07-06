"""Generated from Smithy shape ``com.amazonaws.mq#ForbiddenException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mq.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class ForbiddenException_(TypedDict, closed=True):
    error_attribute: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The attribute which caused the error.</p>"""
    message: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The explanation of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForbiddenException_) -> dict:
    out: dict = {}
    if "error_attribute" in value:
        out["errorAttribute"] = value["error_attribute"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ForbiddenException_:
    out: ForbiddenException_ = {}  # type: ignore[typeddict-item]
    if "errorAttribute" in data:
        out["error_attribute"] = data["errorAttribute"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ForbiddenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mq#ForbiddenException``."""

    code: str | None = "ForbiddenException"

    def __init__(self, data: ForbiddenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ForbiddenException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ForbiddenException":
        return cls(deserialize_json(data))
