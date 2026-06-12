"""Generated from Smithy shape ``com.amazonaws.greengrass#InternalServerErrorException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_greengrass.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.error_details


class InternalServerErrorException_(TypedDict):
    error_details: NotRequired["aws_sdk_greengrass.types.error_details.ErrorDetails"]
    """Details about the error."""
    message: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A message containing information about the error."""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    if "error_details" in value:
        import aws_sdk_greengrass.types.error_details

        out["ErrorDetails"] = aws_sdk_greengrass.types.error_details.serialize_json(
            value["error_details"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    if "ErrorDetails" in data:
        import aws_sdk_greengrass.types.error_details

        out["error_details"] = aws_sdk_greengrass.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.greengrass#InternalServerErrorException``."""

    code: str | None = "InternalServerErrorException"

    def __init__(self, data: InternalServerErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerErrorException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerErrorException":
        return cls(deserialize_json(data))
