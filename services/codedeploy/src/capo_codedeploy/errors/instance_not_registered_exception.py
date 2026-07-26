"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceNotRegisteredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import capo_codedeploy.types.message


class InstanceNotRegisteredException_(TypedDict, closed=True):
    message: NotRequired["capo_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceNotRegisteredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceNotRegisteredException_:
    out: InstanceNotRegisteredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InstanceNotRegisteredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InstanceNotRegisteredException``."""

    code: str | None = "InstanceNotRegisteredException"

    def __init__(self, data: InstanceNotRegisteredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InstanceNotRegisteredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InstanceNotRegisteredException":
        return cls(deserialize_aws_json_1_1(data))
