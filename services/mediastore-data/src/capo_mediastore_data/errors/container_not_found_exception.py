"""Generated from Smithy shape ``com.amazonaws.mediastoredata#ContainerNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediastore_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediastore_data.types.error_message


class ContainerNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_mediastore_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ContainerNotFoundException_:
    out: ContainerNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ContainerNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastoredata#ContainerNotFoundException``."""

    code: str | None = "ContainerNotFoundException"

    def __init__(self, data: ContainerNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContainerNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ContainerNotFoundException":
        return cls(deserialize_json(data))
