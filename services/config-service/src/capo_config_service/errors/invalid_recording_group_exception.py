"""Generated from Smithy shape ``com.amazonaws.configservice#InvalidRecordingGroupException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.error_message


class InvalidRecordingGroupException_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRecordingGroupException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRecordingGroupException_:
    out: InvalidRecordingGroupException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidRecordingGroupException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#InvalidRecordingGroupException``."""

    code: str | None = "InvalidRecordingGroupException"

    def __init__(self, data: InvalidRecordingGroupException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRecordingGroupException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidRecordingGroupException":
        return cls(deserialize_aws_json_1_1(data))
