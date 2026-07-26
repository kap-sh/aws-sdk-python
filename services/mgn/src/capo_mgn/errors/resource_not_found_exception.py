"""Generated from Smithy shape ``com.amazonaws.mgn#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import ServiceError

if TYPE_CHECKING:
    import capo_mgn.types.large_bounded_string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    code: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    resource_id: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Resource ID not found error.</p>"""
    resource_type: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Resource type not found error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mgn#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_json(data))
