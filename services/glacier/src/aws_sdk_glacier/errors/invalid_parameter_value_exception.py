"""Generated from Smithy shape ``com.amazonaws.glacier#InvalidParameterValueException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glacier.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class InvalidParameterValueException_(TypedDict):
    type: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Client</p>"""
    code: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>400 Bad Request</p>"""
    message: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Returned if a parameter of the request is incorrectly specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterValueException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterValueException_:
    out: InvalidParameterValueException_ = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidParameterValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#InvalidParameterValueException``."""

    code: str | None = "InvalidParameterValueException"

    def __init__(self, data: InvalidParameterValueException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterValueException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidParameterValueException":
        return cls(deserialize_json(data))
