"""Generated from Smithy shape ``com.amazonaws.connect#MaximumResultReturnedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_connect.types.message


class MaximumResultReturnedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_connect.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: MaximumResultReturnedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MaximumResultReturnedException_:
    out: MaximumResultReturnedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class MaximumResultReturnedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#MaximumResultReturnedException``."""

    code: str | None = "MaximumResultReturnedException"

    def __init__(self, data: MaximumResultReturnedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MaximumResultReturnedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MaximumResultReturnedException":
        return cls(deserialize_json(data))
