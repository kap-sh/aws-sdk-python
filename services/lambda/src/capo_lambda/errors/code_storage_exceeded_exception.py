"""Generated from Smithy shape ``com.amazonaws.lambda#CodeStorageExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class CodeStorageExceededException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeStorageExceededException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CodeStorageExceededException_:
    out: CodeStorageExceededException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CodeStorageExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#CodeStorageExceededException``."""

    code: str | None = "CodeStorageExceededException"

    def __init__(self, data: CodeStorageExceededException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CodeStorageExceededException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "CodeStorageExceededException":
        return cls(deserialize_json(data), message)
