"""Generated from Smithy shape ``com.amazonaws.workspaces#OperationNotSupportedException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.exception_error_code
    import aws_sdk_workspaces.types.exception_message


class OperationNotSupportedException_(TypedDict):
    message: NotRequired["aws_sdk_workspaces.types.exception_message.ExceptionMessage"]
    """<p>The exception error message.</p>"""
    reason: NotRequired[
        "aws_sdk_workspaces.types.exception_error_code.ExceptionErrorCode"
    ]
    """<p>The exception error reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationNotSupportedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationNotSupportedException_:
    out: OperationNotSupportedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out


class OperationNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#OperationNotSupportedException``."""

    code: str | None = "OperationNotSupportedException"

    def __init__(self, data: OperationNotSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperationNotSupportedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OperationNotSupportedException":
        return cls(deserialize_aws_json_1_1(data))
