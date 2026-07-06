"""Generated from Smithy shape ``com.amazonaws.oam#MissingRequiredParameterException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_oam.errors import ServiceError


class MissingRequiredParameterException_(TypedDict, closed=True):
    message: NotRequired["str"]
    amzn_error_type: NotRequired["str"]
    """<p>The name of the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingRequiredParameterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MissingRequiredParameterException_:
    out: MissingRequiredParameterException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MissingRequiredParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.oam#MissingRequiredParameterException``."""

    code: str | None = "MissingRequiredParameterException"

    def __init__(self, data: MissingRequiredParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingRequiredParameterException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MissingRequiredParameterException":
        return cls(deserialize_json(data))
