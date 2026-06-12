"""Generated from Smithy shape ``com.amazonaws.outposts#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_outposts.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.error_message
    import aws_sdk_outposts.types.resource_type
    import aws_sdk_outposts.types.string


class ConflictException_(TypedDict):
    message: NotRequired["aws_sdk_outposts.types.error_message.ErrorMessage"]
    resource_id: NotRequired["aws_sdk_outposts.types.string.String"]
    """<p>The ID of the resource causing the conflict.</p>"""
    resource_type: NotRequired["aws_sdk_outposts.types.resource_type.ResourceType"]
    """<p>The type of the resource causing the conflict.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        import aws_sdk_outposts.types.resource_type

        out["ResourceType"] = aws_sdk_outposts.types.resource_type.serialize_json(
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
        import aws_sdk_outposts.types.resource_type

        out["resource_type"] = aws_sdk_outposts.types.resource_type.deserialize_json(
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
