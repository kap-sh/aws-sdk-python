"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#AuthException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.string


class AuthException_(TypedDict, closed=True):
    message: NotRequired["capo_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthException_:
    out: AuthException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AuthException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#AuthException``."""

    code: str | None = "AuthException"

    def __init__(self, data: AuthException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AuthException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AuthException":
        return cls(deserialize_aws_json_1_1(data))
