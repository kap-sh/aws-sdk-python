"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#EC2InstanceTypeInvalidException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ec2_instance_connect.types.string


class EC2InstanceTypeInvalidException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2InstanceTypeInvalidException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2InstanceTypeInvalidException_:
    out: EC2InstanceTypeInvalidException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EC2InstanceTypeInvalidException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#EC2InstanceTypeInvalidException``."""

    code: str | None = "EC2InstanceTypeInvalidException"

    def __init__(self, data: EC2InstanceTypeInvalidException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EC2InstanceTypeInvalidException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EC2InstanceTypeInvalidException":
        return cls(deserialize_aws_json_1_1(data))
