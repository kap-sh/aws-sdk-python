"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ResourceNotFoundException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography.errors import ServiceError


class ResourceNotFoundException_(TypedDict, closed=True):
    resource_id: NotRequired["str"]
    """<p>The identifier of the resource that was not found.</p> <p>This field contains the specific resource identifier (such as a key ARN or alias name) that could not be located.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.paymentcryptography#ResourceNotFoundException``."""

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
