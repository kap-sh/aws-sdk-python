"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_agreement.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.exception_message
    import aws_sdk_marketplace_agreement.types.request_id
    import aws_sdk_marketplace_agreement.types.resource_id
    import aws_sdk_marketplace_agreement.types.resource_type


class ConflictException_(TypedDict):
    request_id: NotRequired["aws_sdk_marketplace_agreement.types.request_id.RequestId"]
    """<p>The unique identifier for the error.</p>"""
    message: NotRequired[
        "aws_sdk_marketplace_agreement.types.exception_message.ExceptionMessage"
    ]
    """<p>Description of the error.</p>"""
    resource_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the resource involved in the conflict.</p>"""
    resource_type: NotRequired[
        "aws_sdk_marketplace_agreement.types.resource_type.ResourceType"
    ]
    """<p>The type of the resource involved in the conflict.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        import aws_sdk_marketplace_agreement.types.resource_type

        out["resourceType"] = (
            aws_sdk_marketplace_agreement.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        import aws_sdk_marketplace_agreement.types.resource_type

        out["resource_type"] = (
            aws_sdk_marketplace_agreement.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceagreement#ConflictException``."""

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
