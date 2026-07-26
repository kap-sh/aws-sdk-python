"""Generated from Smithy shape ``com.amazonaws.backup#DependencyFailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import ServiceError

if TYPE_CHECKING:
    import capo_backup.types.string


class DependencyFailureException_(TypedDict, closed=True):
    code: NotRequired["capo_backup.types.string.string"]
    message: NotRequired["capo_backup.types.string.string"]
    type: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""
    context: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyFailureException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "type" in value:
        out["Type"] = value["type"]
    if "context" in value:
        out["Context"] = value["context"]
    return out


def deserialize_json(data: dict) -> DependencyFailureException_:
    out: DependencyFailureException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Context" in data:
        out["context"] = data["Context"]
    return out


class DependencyFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backup#DependencyFailureException``."""

    code: str | None = "DependencyFailureException"

    def __init__(self, data: DependencyFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DependencyFailureException":
        return cls(deserialize_json(data))
