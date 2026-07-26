"""Generated from Smithy shape ``com.amazonaws.mq#InternalServerErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mq.errors import ServiceError

if TYPE_CHECKING:
    import capo_mq.types.__string


class InternalServerErrorException_(TypedDict, closed=True):
    error_attribute: NotRequired["capo_mq.types.__string.__string"]
    """<p>The attribute which caused the error.</p>"""
    message: NotRequired["capo_mq.types.__string.__string"]
    """<p>The explanation of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    if "error_attribute" in value:
        out["errorAttribute"] = value["error_attribute"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    if "errorAttribute" in data:
        out["error_attribute"] = data["errorAttribute"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mq#InternalServerErrorException``."""

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
