"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mwaa_serverless.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.error_message


class ConflictException_(TypedDict, closed=True):
    message: "capo_mwaa_serverless.types.error_message.ErrorMessage"
    resource_id: "str"
    """<p>The unique identifier of the resource.</p>"""
    resource_type: "str"
    """<p>The type of the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mwaaserverless#ConflictException``."""

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
