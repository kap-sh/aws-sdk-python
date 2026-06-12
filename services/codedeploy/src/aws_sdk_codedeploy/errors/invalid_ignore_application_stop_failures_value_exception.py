"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidIgnoreApplicationStopFailuresValueException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.message


class InvalidIgnoreApplicationStopFailuresValueException_(TypedDict):
    message: NotRequired["aws_sdk_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InvalidIgnoreApplicationStopFailuresValueException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> InvalidIgnoreApplicationStopFailuresValueException_:
    out: InvalidIgnoreApplicationStopFailuresValueException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidIgnoreApplicationStopFailuresValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidIgnoreApplicationStopFailuresValueException``."""

    code: str | None = "InvalidIgnoreApplicationStopFailuresValueException"

    def __init__(self, data: InvalidIgnoreApplicationStopFailuresValueException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidIgnoreApplicationStopFailuresValueException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "InvalidIgnoreApplicationStopFailuresValueException":
        return cls(deserialize_aws_json_1_1(data))
