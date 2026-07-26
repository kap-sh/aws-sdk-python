"""Generated from Smithy shape ``com.amazonaws.amplifybackend#NotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifybackend.errors import ServiceError

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class NotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>An error message to inform that the request has failed.</p>"""
    resource_type: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The type of resource that is not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.amplifybackend#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(self, data: NotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotFoundException":
        return cls(deserialize_json(data))
