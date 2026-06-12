"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CloudHsmServiceException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudhsm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.boolean
    import aws_sdk_cloudhsm.types.string


class CloudHsmServiceException_(TypedDict):
    message: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>Additional information about the error.</p>"""
    retryable: "aws_sdk_cloudhsm.types.boolean.Boolean"
    """<p>Indicates if the action can be retried.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["retryable"] = value.get("retryable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmServiceException_:
    out: CloudHsmServiceException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "retryable" in data:
        out["retryable"] = data["retryable"]
    else:
        out["retryable"] = False
    return out


class CloudHsmServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsm#CloudHsmServiceException``."""

    code: str | None = "CloudHsmServiceException"

    def __init__(self, data: CloudHsmServiceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmServiceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CloudHsmServiceException":
        return cls(deserialize_aws_json_1_1(data))
