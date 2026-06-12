"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidResultAttributeException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidResultAttributeException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidResultAttributeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidResultAttributeException_:
    out: InvalidResultAttributeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidResultAttributeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidResultAttributeException``."""

    code: str | None = "InvalidResultAttributeException"

    def __init__(self, data: InvalidResultAttributeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResultAttributeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidResultAttributeException":
        return cls(deserialize_aws_json_1_1(data))
