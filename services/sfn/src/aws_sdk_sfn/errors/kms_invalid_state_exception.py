"""Generated from Smithy shape ``com.amazonaws.sfn#KmsInvalidStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.error_message
    import aws_sdk_sfn.types.kms_key_state


class KmsInvalidStateException_(TypedDict, closed=True):
    kms_key_state: NotRequired["aws_sdk_sfn.types.kms_key_state.KmsKeyState"]
    """<p>Current status of the KMS; key. For example: <code>DISABLED</code>, <code>PENDING_DELETION</code>, <code>PENDING_IMPORT</code>, <code>UNAVAILABLE</code>, <code>CREATING</code>.</p>"""
    message: NotRequired["aws_sdk_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsInvalidStateException_) -> dict:
    out: dict = {}
    if "kms_key_state" in value:
        import aws_sdk_sfn.types.kms_key_state

        out["kmsKeyState"] = aws_sdk_sfn.types.kms_key_state.serialize_aws_json_1_0(
            value["kms_key_state"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsInvalidStateException_:
    out: KmsInvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "kmsKeyState" in data:
        import aws_sdk_sfn.types.kms_key_state

        out["kms_key_state"] = aws_sdk_sfn.types.kms_key_state.deserialize_aws_json_1_0(
            data["kmsKeyState"]
        )
    if "message" in data:
        out["message"] = data["message"]
    return out


class KmsInvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#KmsInvalidStateException``."""

    code: str | None = "KmsInvalidStateException"

    def __init__(self, data: KmsInvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsInvalidStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "KmsInvalidStateException":
        return cls(deserialize_aws_json_1_0(data))
