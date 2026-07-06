"""Generated from Smithy shape ``com.amazonaws.servicecatalog#InvalidStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.error_message


class InvalidStateException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_service_catalog.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidStateException_:
    out: InvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicecatalog#InvalidStateException``."""

    code: str | None = "InvalidStateException"

    def __init__(self, data: InvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidStateException":
        return cls(deserialize_aws_json_1_1(data))
