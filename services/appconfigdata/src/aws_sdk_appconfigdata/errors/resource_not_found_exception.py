"""Generated from Smithy shape ``com.amazonaws.appconfigdata#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appconfigdata.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appconfigdata.types.resource_type
    import aws_sdk_appconfigdata.types.string
    import aws_sdk_appconfigdata.types.string_map


class ResourceNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_appconfigdata.types.string.String"]
    resource_type: NotRequired["aws_sdk_appconfigdata.types.resource_type.ResourceType"]
    """<p>The type of resource that was not found.</p>"""
    referenced_by: NotRequired["aws_sdk_appconfigdata.types.string_map.StringMap"]
    """<p>A map indicating which parameters in the request reference the resource that was not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "referenced_by" in value:
        import aws_sdk_appconfigdata.types.string_map

        out["ReferencedBy"] = aws_sdk_appconfigdata.types.string_map.serialize_json(
            value["referenced_by"]
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ReferencedBy" in data:
        import aws_sdk_appconfigdata.types.string_map

        out["referenced_by"] = aws_sdk_appconfigdata.types.string_map.deserialize_json(
            data["ReferencedBy"]
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appconfigdata#ResourceNotFoundException``."""

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
