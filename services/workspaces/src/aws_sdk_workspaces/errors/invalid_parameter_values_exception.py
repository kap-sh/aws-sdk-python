"""Generated from Smithy shape ``com.amazonaws.workspaces#InvalidParameterValuesException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.exception_message


class InvalidParameterValuesException_(TypedDict):
    message: NotRequired["aws_sdk_workspaces.types.exception_message.ExceptionMessage"]
    """<p>The exception error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParameterValuesException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParameterValuesException_:
    out: InvalidParameterValuesException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidParameterValuesException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#InvalidParameterValuesException``."""

    code: str | None = "InvalidParameterValuesException"

    def __init__(self, data: InvalidParameterValuesException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterValuesException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidParameterValuesException":
        return cls(deserialize_aws_json_1_1(data))
