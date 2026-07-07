"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#InternalServiceException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_catalog.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.exception_message_content


class InternalServiceException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_marketplace_catalog.types.exception_message_content.ExceptionMessageContent"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServiceException_:
    out: InternalServiceException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacecatalog#InternalServiceException``."""

    code: str | None = "InternalServiceException"

    def __init__(self, data: InternalServiceException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServiceException":
        return cls(deserialize_json(data))
