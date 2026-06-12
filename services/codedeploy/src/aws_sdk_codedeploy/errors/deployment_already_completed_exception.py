"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentAlreadyCompletedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.message


class DeploymentAlreadyCompletedException_(TypedDict):
    message: NotRequired["aws_sdk_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentAlreadyCompletedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentAlreadyCompletedException_:
    out: DeploymentAlreadyCompletedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DeploymentAlreadyCompletedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#DeploymentAlreadyCompletedException``."""

    code: str | None = "DeploymentAlreadyCompletedException"

    def __init__(self, data: DeploymentAlreadyCompletedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeploymentAlreadyCompletedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DeploymentAlreadyCompletedException":
        return cls(deserialize_aws_json_1_1(data))
