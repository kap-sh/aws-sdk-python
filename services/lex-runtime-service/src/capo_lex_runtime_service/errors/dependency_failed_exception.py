"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#DependencyFailedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.error_message


class DependencyFailedException_(TypedDict, closed=True):
    message: NotRequired["capo_lex_runtime_service.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependencyFailedException_:
    out: DependencyFailedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DependencyFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimeservice#DependencyFailedException``."""

    code: str | None = "DependencyFailedException"

    def __init__(self, data: DependencyFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyFailedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DependencyFailedException":
        return cls(deserialize_json(data))
