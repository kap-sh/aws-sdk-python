"""Generated from Smithy shape ``com.amazonaws.clouddirectory#InvalidFacetUpdateException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.exception_message


class InvalidFacetUpdateException_(TypedDict):
    message: NotRequired[
        "aws_sdk_clouddirectory.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidFacetUpdateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidFacetUpdateException_:
    out: InvalidFacetUpdateException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidFacetUpdateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#InvalidFacetUpdateException``."""

    code: str | None = "InvalidFacetUpdateException"

    def __init__(self, data: InvalidFacetUpdateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFacetUpdateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidFacetUpdateException":
        return cls(deserialize_json(data))
