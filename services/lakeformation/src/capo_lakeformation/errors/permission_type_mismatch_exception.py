"""Generated from Smithy shape ``com.amazonaws.lakeformation#PermissionTypeMismatchException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_lakeformation.types.message_string


class PermissionTypeMismatchException_(TypedDict, closed=True):
    message: NotRequired["capo_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTypeMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PermissionTypeMismatchException_:
    out: PermissionTypeMismatchException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PermissionTypeMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#PermissionTypeMismatchException``."""

    code: str | None = "PermissionTypeMismatchException"

    def __init__(self, data: PermissionTypeMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PermissionTypeMismatchException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PermissionTypeMismatchException":
        return cls(deserialize_json(data))
