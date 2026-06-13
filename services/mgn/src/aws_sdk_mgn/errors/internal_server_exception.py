"""Generated from Smithy shape ``com.amazonaws.mgn#InternalServerException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mgn.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.large_bounded_string
    import aws_sdk_mgn.types.positive_integer


class InternalServerException_(TypedDict):
    message: "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    retry_after_seconds: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>The server encountered an unexpected condition that prevented it from fulfilling the request. The request will be retried again after x seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mgn#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))
