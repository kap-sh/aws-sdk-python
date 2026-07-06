"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.exception_message
    import aws_sdk_ssm_incidents.types.resource_type


class ConflictException_(TypedDict, closed=True):
    message: "aws_sdk_ssm_incidents.types.exception_message.ExceptionMessage"
    resource_identifier: NotRequired["str"]
    """The identifier of the requested resource"""
    resource_type: NotRequired["aws_sdk_ssm_incidents.types.resource_type.ResourceType"]
    """The resource type"""
    retry_after: NotRequired["datetime.datetime"]
    """If present in the output, the operation can be retried after this time"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_identifier" in value:
        out["resourceIdentifier"] = value["resource_identifier"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "retry_after" in value:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["retryAfter"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["retry_after"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "resourceIdentifier" in data:
        out["resource_identifier"] = data["resourceIdentifier"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "retryAfter" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["retry_after"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["retryAfter"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmincidents#ConflictException``."""

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
