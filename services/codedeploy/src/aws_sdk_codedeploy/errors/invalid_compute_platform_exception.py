"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidComputePlatformException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.message


class InvalidComputePlatformException_(TypedDict):
    message: NotRequired["aws_sdk_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidComputePlatformException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidComputePlatformException_:
    out: InvalidComputePlatformException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidComputePlatformException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidComputePlatformException``."""

    code: str | None = "InvalidComputePlatformException"

    def __init__(self, data: InvalidComputePlatformException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidComputePlatformException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidComputePlatformException":
        return cls(deserialize_aws_json_1_1(data))
