"""Generated from Smithy shape ``com.amazonaws.groundstation#InvalidParameterException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import ServiceError


class InvalidParameterException_(TypedDict):
    message: NotRequired["str"]
    parameter_name: NotRequired["str"]
    """<p>Name of the invalid parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "parameter_name" in value:
        out["parameterName"] = value["parameter_name"]
    return out


def deserialize_json(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "parameterName" in data:
        out["parameter_name"] = data["parameterName"]
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.groundstation#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(self, data: InvalidParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidParameterException":
        return cls(deserialize_json(data))
