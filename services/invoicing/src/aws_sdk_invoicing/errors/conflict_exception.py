"""Generated from Smithy shape ``com.amazonaws.invoicing#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_invoicing.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string


class ConflictException_(TypedDict):
    message: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    resource_id: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p>The identifier of the resource that caused the conflict.</p>"""
    resource_type: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p>The type of resource that caused the conflict.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.invoicing#ConflictException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "ConflictException":
        return cls(deserialize_aws_json_1_0(data))
