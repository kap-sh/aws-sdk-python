"""Generated from Smithy shape ``com.amazonaws.glue#IllegalWorkflowStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.message_string


class IllegalWorkflowStateException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IllegalWorkflowStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IllegalWorkflowStateException_:
    out: IllegalWorkflowStateException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IllegalWorkflowStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#IllegalWorkflowStateException``."""

    code: str | None = "IllegalWorkflowStateException"

    def __init__(self, data: IllegalWorkflowStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalWorkflowStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IllegalWorkflowStateException":
        return cls(deserialize_aws_json_1_1(data))
