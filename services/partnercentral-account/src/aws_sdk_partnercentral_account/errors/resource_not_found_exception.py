"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.resource_not_found_exception_reason


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "str"
    reason: "aws_sdk_partnercentral_account.types.resource_not_found_exception_reason.ResourceNotFoundExceptionReason"
    """<p>The specific reason why the resource was not found.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import aws_sdk_partnercentral_account.types.resource_not_found_exception_reason

    out["Reason"] = (
        aws_sdk_partnercentral_account.types.resource_not_found_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if "Reason" in data:
        import aws_sdk_partnercentral_account.types.resource_not_found_exception_reason

        out["reason"] = (
            aws_sdk_partnercentral_account.types.resource_not_found_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ResourceNotFoundException_.reason required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralaccount#ResourceNotFoundException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_0(data))
