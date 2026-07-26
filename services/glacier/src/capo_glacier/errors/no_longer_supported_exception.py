"""Generated from Smithy shape ``com.amazonaws.glacier#NoLongerSupportedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glacier.errors import ServiceError

if TYPE_CHECKING:
    import capo_glacier.types.string


class NoLongerSupportedException_(TypedDict, closed=True):
    type: NotRequired["capo_glacier.types.string.string"]
    """<p>Client</p>"""
    code: NotRequired["capo_glacier.types.string.string"]
    """<p>400 Bad Request</p>"""
    message: NotRequired["capo_glacier.types.string.string"]
    """<p>This API is no longer supported for new accounts. Please use Amazon S3 Glacier storage classes instead.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NoLongerSupportedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NoLongerSupportedException_:
    out: NoLongerSupportedException_ = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NoLongerSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#NoLongerSupportedException``."""

    code: str | None = "NoLongerSupportedException"

    def __init__(self, data: NoLongerSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoLongerSupportedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NoLongerSupportedException":
        return cls(deserialize_json(data))
