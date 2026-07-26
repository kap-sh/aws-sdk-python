"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ServiceException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import ServiceError

if TYPE_CHECKING:
    import capo_imagebuilder.types.error_message


class ServiceException_(TypedDict, closed=True):
    message: NotRequired["capo_imagebuilder.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceException_:
    out: ServiceException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.imagebuilder#ServiceException``."""

    code: str | None = "ServiceException"

    def __init__(self, data: ServiceException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceException":
        return cls(deserialize_json(data))
