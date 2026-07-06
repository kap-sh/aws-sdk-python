"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidApplicationNameException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.message


class InvalidApplicationNameException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidApplicationNameException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidApplicationNameException_:
    out: InvalidApplicationNameException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidApplicationNameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidApplicationNameException``."""

    code: str | None = "InvalidApplicationNameException"

    def __init__(self, data: InvalidApplicationNameException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidApplicationNameException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidApplicationNameException":
        return cls(deserialize_aws_json_1_1(data))
