"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionRequiredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.message


class RevisionRequiredException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RevisionRequiredException_:
    out: RevisionRequiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RevisionRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#RevisionRequiredException``."""

    code: str | None = "RevisionRequiredException"

    def __init__(self, data: RevisionRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RevisionRequiredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RevisionRequiredException":
        return cls(deserialize_aws_json_1_1(data))
