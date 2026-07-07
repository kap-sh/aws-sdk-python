"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidFileExistsBehaviorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.message


class InvalidFileExistsBehaviorException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFileExistsBehaviorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFileExistsBehaviorException_:
    out: InvalidFileExistsBehaviorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidFileExistsBehaviorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidFileExistsBehaviorException``."""

    code: str | None = "InvalidFileExistsBehaviorException"

    def __init__(self, data: InvalidFileExistsBehaviorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFileExistsBehaviorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidFileExistsBehaviorException":
        return cls(deserialize_aws_json_1_1(data))
