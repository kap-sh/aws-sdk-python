"""Generated from Smithy shape ``com.amazonaws.quicksight#ResourceUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import capo_quicksight.types.exception_resource_type
    import capo_quicksight.types.string


class ResourceUnavailableException_(TypedDict, closed=True):
    message: NotRequired["capo_quicksight.types.string.String"]
    resource_type: NotRequired[
        "capo_quicksight.types.exception_resource_type.ExceptionResourceType"
    ]
    """<p>The resource type for this request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        import capo_quicksight.types.exception_resource_type

        out["ResourceType"] = (
            capo_quicksight.types.exception_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ResourceUnavailableException_:
    out: ResourceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceType" in data:
        import capo_quicksight.types.exception_resource_type

        out["resource_type"] = (
            capo_quicksight.types.exception_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class ResourceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#ResourceUnavailableException``."""

    code: str | None = "ResourceUnavailableException"

    def __init__(self, data: ResourceUnavailableException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceUnavailableException":
        return cls(deserialize_json(data))
