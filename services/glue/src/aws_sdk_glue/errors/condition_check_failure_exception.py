"""Generated from Smithy shape ``com.amazonaws.glue#ConditionCheckFailureException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class ConditionCheckFailureException_(TypedDict):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionCheckFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionCheckFailureException_:
    out: ConditionCheckFailureException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ConditionCheckFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#ConditionCheckFailureException``."""

    code: str | None = "ConditionCheckFailureException"

    def __init__(self, data: ConditionCheckFailureException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConditionCheckFailureException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ConditionCheckFailureException":
        return cls(deserialize_aws_json_1_1(data))
