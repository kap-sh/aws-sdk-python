"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectparticipant.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.message
    import aws_sdk_connectparticipant.types.resource_id
    import aws_sdk_connectparticipant.types.resource_type


class ResourceNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_connectparticipant.types.message.Message"]
    resource_id: NotRequired["aws_sdk_connectparticipant.types.resource_id.ResourceId"]
    """<p>The identifier of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_connectparticipant.types.resource_type.ResourceType"
    ]
    """<p>The type of Connect Customer resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        import aws_sdk_connectparticipant.types.resource_type

        out["ResourceType"] = (
            aws_sdk_connectparticipant.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        import aws_sdk_connectparticipant.types.resource_type

        out["resource_type"] = (
            aws_sdk_connectparticipant.types.resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectparticipant#ResourceNotFoundException``."""

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
