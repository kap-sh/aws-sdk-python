"""Generated from Smithy shape ``com.amazonaws.ecr#KmsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message
    import aws_sdk_ecr.types.kms_error


class KmsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]
    kms_error: NotRequired["aws_sdk_ecr.types.kms_error.KmsError"]
    """<p>The error code returned by KMS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KmsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "kms_error" in value:
        out["kmsError"] = value["kms_error"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KmsException_:
    out: KmsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "kmsError" in data:
        out["kms_error"] = data["kmsError"]
    return out


class KmsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#KmsException``."""

    code: str | None = "KmsException"

    def __init__(self, data: KmsException_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="KmsException"
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KmsException":
        return cls(deserialize_aws_json_1_1(data))
