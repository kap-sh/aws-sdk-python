"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.string


class ConflictException_(TypedDict, closed=True):
    message: "aws_sdk_iotfleetwise.types.string.string"
    resource: "aws_sdk_iotfleetwise.types.string.string"
    """<p>The resource on which there are conflicting operations.</p>"""
    resource_type: "aws_sdk_iotfleetwise.types.string.string"
    """<p>The type of resource on which there are conflicting operations..</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resource"] = value["resource"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "resource" in data:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("ConflictException_.resource required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#ConflictException``."""

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
