"""Generated from Smithy shape ``com.amazonaws.chime#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime.types.error_code
    import capo_chime.types.string


class ConflictException_(TypedDict, closed=True):
    code: NotRequired["capo_chime.types.error_code.ErrorCode"]
    message: NotRequired["capo_chime.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_chime.types.error_code

        out["Code"] = capo_chime.types.error_code.serialize_json(value["code"])
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_chime.types.error_code

        out["code"] = capo_chime.types.error_code.deserialize_json(data["Code"])
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chime#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
