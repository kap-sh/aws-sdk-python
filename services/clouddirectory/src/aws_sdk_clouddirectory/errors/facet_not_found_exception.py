"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.exception_message


class FacetNotFoundException_(TypedDict):
    message: NotRequired[
        "aws_sdk_clouddirectory.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FacetNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FacetNotFoundException_:
    out: FacetNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FacetNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#FacetNotFoundException``."""

    code: str | None = "FacetNotFoundException"

    def __init__(self, data: FacetNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FacetNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "FacetNotFoundException":
        return cls(deserialize_json(data))
