"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentTargetIdRequiredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import capo_codedeploy.types.message


class DeploymentTargetIdRequiredException_(TypedDict, closed=True):
    message: NotRequired["capo_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentTargetIdRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentTargetIdRequiredException_:
    out: DeploymentTargetIdRequiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DeploymentTargetIdRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#DeploymentTargetIdRequiredException``."""

    code: str | None = "DeploymentTargetIdRequiredException"

    def __init__(self, data: DeploymentTargetIdRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeploymentTargetIdRequiredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DeploymentTargetIdRequiredException":
        return cls(deserialize_aws_json_1_1(data))
