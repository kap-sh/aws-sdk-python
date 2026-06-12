"""Generated from Smithy shape ``com.amazonaws.servicecatalog#InvalidParametersException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.error_message


class InvalidParametersException_(TypedDict):
    message: NotRequired["aws_sdk_service_catalog.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParametersException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParametersException_:
    out: InvalidParametersException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidParametersException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicecatalog#InvalidParametersException``."""

    code: str | None = "InvalidParametersException"

    def __init__(self, data: InvalidParametersException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParametersException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidParametersException":
        return cls(deserialize_aws_json_1_1(data))
