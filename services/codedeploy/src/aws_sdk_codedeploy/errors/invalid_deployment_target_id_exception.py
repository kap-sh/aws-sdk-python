"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidDeploymentTargetIdException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.message


class InvalidDeploymentTargetIdException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidDeploymentTargetIdException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidDeploymentTargetIdException_:
    out: InvalidDeploymentTargetIdException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidDeploymentTargetIdException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidDeploymentTargetIdException``."""

    code: str | None = "InvalidDeploymentTargetIdException"

    def __init__(self, data: InvalidDeploymentTargetIdException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDeploymentTargetIdException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidDeploymentTargetIdException":
        return cls(deserialize_aws_json_1_1(data))
