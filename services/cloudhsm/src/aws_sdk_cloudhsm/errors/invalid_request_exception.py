"""Generated from Smithy shape ``com.amazonaws.cloudhsm#InvalidRequestException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudhsm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.boolean
    import aws_sdk_cloudhsm.types.string


class InvalidRequestException_(TypedDict):
    message: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>Additional information about the error.</p>"""
    retryable: "aws_sdk_cloudhsm.types.boolean.Boolean"
    """<p>Indicates if the action can be retried.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["retryable"] = value.get("retryable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "retryable" in data:
        out["retryable"] = data["retryable"]
    else:
        out["retryable"] = False
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsm#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidRequestException":
        return cls(deserialize_aws_json_1_1(data))
