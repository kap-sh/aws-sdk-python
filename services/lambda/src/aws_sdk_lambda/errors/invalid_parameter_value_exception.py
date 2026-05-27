"""Generated from Smithy shape ``com.amazonaws.lambda#InvalidParameterValueException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class InvalidParameterValueException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterValueException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterValueException_:
    out: InvalidParameterValueException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidParameterValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#InvalidParameterValueException``."""

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
