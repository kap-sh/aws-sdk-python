"""Generated from Smithy shape ``com.amazonaws.lambda#PreconditionFailedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class PreconditionFailedException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["capo_lambda.types.string.String"]
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreconditionFailedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PreconditionFailedException_:
    out: PreconditionFailedException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PreconditionFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#PreconditionFailedException``."""

    code: str | None = "PreconditionFailedException"

    def __init__(self, data: PreconditionFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PreconditionFailedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PreconditionFailedException":
        return cls(deserialize_json(data))
