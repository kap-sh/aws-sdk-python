"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#EC2InstanceStateInvalidException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.string


class EC2InstanceStateInvalidException_(TypedDict, closed=True):
    message: NotRequired["capo_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2InstanceStateInvalidException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2InstanceStateInvalidException_:
    out: EC2InstanceStateInvalidException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EC2InstanceStateInvalidException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#EC2InstanceStateInvalidException``."""

    code: str | None = "EC2InstanceStateInvalidException"

    def __init__(self, data: EC2InstanceStateInvalidException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EC2InstanceStateInvalidException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EC2InstanceStateInvalidException":
        return cls(deserialize_aws_json_1_1(data))
