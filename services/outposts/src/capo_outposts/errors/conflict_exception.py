"""Generated from Smithy shape ``com.amazonaws.outposts#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_outposts.errors import ServiceError

if TYPE_CHECKING:
    import capo_outposts.types.error_message
    import capo_outposts.types.resource_type
    import capo_outposts.types.string


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_outposts.types.error_message.ErrorMessage"]
    resource_id: NotRequired["capo_outposts.types.string.String"]
    """<p>The ID of the resource causing the conflict.</p>"""
    resource_type: NotRequired["capo_outposts.types.resource_type.ResourceType"]
    """<p>The type of the resource causing the conflict.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        import capo_outposts.types.resource_type

        out["ResourceType"] = capo_outposts.types.resource_type.serialize_json(
            value["resource_type"]
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        import capo_outposts.types.resource_type

        out["resource_type"] = capo_outposts.types.resource_type.deserialize_json(
            data["ResourceType"]
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.outposts#ConflictException``."""

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
