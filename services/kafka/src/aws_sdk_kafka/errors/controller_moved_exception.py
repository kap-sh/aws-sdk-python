"""Generated from Smithy shape ``com.amazonaws.kafka#ControllerMovedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kafka.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class ControllerMovedException_(TypedDict):
    invalid_parameter: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The parameter that caused the error.</p>"""
    message: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControllerMovedException_) -> dict:
    out: dict = {}
    if "invalid_parameter" in value:
        out["invalidParameter"] = value["invalid_parameter"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ControllerMovedException_:
    out: ControllerMovedException_ = {}  # type: ignore[typeddict-item]
    if "invalidParameter" in data:
        out["invalid_parameter"] = data["invalidParameter"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ControllerMovedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kafka#ControllerMovedException``."""

    code: str | None = "ControllerMovedException"

    def __init__(self, data: ControllerMovedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ControllerMovedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ControllerMovedException":
        return cls(deserialize_json(data))
