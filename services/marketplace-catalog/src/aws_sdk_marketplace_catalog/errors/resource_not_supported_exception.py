"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResourceNotSupportedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_catalog.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.exception_message_content


class ResourceNotSupportedException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_marketplace_catalog.types.exception_message_content.ExceptionMessageContent"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotSupportedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotSupportedException_:
    out: ResourceNotSupportedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacecatalog#ResourceNotSupportedException``."""

    code: str | None = "ResourceNotSupportedException"

    def __init__(self, data: ResourceNotSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotSupportedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotSupportedException":
        return cls(deserialize_json(data))
