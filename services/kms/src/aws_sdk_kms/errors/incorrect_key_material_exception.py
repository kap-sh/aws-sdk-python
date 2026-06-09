"""Generated from Smithy shape ``com.amazonaws.kms#IncorrectKeyMaterialException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class IncorrectKeyMaterialException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncorrectKeyMaterialException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IncorrectKeyMaterialException_:
    out: IncorrectKeyMaterialException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class IncorrectKeyMaterialException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#IncorrectKeyMaterialException``."""

    code: str | None = "IncorrectKeyMaterialException"

    def __init__(self, data: IncorrectKeyMaterialException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncorrectKeyMaterialException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IncorrectKeyMaterialException":
        return cls(deserialize_aws_json_1_1(data))
