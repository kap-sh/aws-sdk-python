"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#LimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.string


class LimitExceededException_(TypedDict, closed=True):
    message: "aws_sdk_iotfleetwise.types.string.string"
    resource_id: "aws_sdk_iotfleetwise.types.string.string"
    """<p>The identifier of the resource that was exceeded.</p>"""
    resource_type: "aws_sdk_iotfleetwise.types.string.string"
    """<p>The type of resource that was exceeded.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("LimitExceededException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("LimitExceededException_.resource_id required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("LimitExceededException_.resource_type required")
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_aws_json_1_0(data))
