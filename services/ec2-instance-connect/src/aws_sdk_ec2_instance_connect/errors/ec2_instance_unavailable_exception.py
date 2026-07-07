"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#EC2InstanceUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ec2_instance_connect.types.string


class EC2InstanceUnavailableException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2InstanceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2InstanceUnavailableException_:
    out: EC2InstanceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EC2InstanceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#EC2InstanceUnavailableException``."""

    code: str | None = "EC2InstanceUnavailableException"

    def __init__(self, data: EC2InstanceUnavailableException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="EC2InstanceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EC2InstanceUnavailableException":
        return cls(deserialize_aws_json_1_1(data))
