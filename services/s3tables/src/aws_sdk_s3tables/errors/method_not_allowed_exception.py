"""Generated from Smithy shape ``com.amazonaws.s3tables#MethodNotAllowedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3tables.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.error_message


class MethodNotAllowedException_(TypedDict):
    message: NotRequired["aws_sdk_s3tables.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MethodNotAllowedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MethodNotAllowedException_:
    out: MethodNotAllowedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MethodNotAllowedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3tables#MethodNotAllowedException``."""

    code: str | None = "MethodNotAllowedException"

    def __init__(self, data: MethodNotAllowedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MethodNotAllowedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MethodNotAllowedException":
        return cls(deserialize_json(data))
