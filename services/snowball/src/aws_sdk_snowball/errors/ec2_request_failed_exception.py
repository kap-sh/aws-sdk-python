"""Generated from Smithy shape ``com.amazonaws.snowball#Ec2RequestFailedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_snowball.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.string


class Ec2RequestFailedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_snowball.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2RequestFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Ec2RequestFailedException_:
    out: Ec2RequestFailedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class Ec2RequestFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#Ec2RequestFailedException``."""

    code: str | None = "Ec2RequestFailedException"

    def __init__(self, data: Ec2RequestFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="Ec2RequestFailedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "Ec2RequestFailedException":
        return cls(deserialize_aws_json_1_1(data))
