"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53_recovery_cluster.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_cluster.types.string


class ConflictException_(TypedDict, closed=True):
    message: "aws_sdk_route53_recovery_cluster.types.string.String"
    """Description of the ConflictException error"""
    resource_id: "aws_sdk_route53_recovery_cluster.types.string.String"
    """Identifier of the resource in use"""
    resource_type: "aws_sdk_route53_recovery_cluster.types.string.String"
    """Type of the resource in use"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53recoverycluster#ConflictException``."""

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
