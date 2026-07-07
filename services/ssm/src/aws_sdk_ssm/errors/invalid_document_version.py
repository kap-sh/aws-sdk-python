"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidDocumentVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidDocumentVersion_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidDocumentVersion_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidDocumentVersion_:
    out: InvalidDocumentVersion_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidDocumentVersion(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidDocumentVersion``."""

    code: str | None = "InvalidDocumentVersion"

    def __init__(self, data: InvalidDocumentVersion_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDocumentVersion",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidDocumentVersion":
        return cls(deserialize_aws_json_1_1(data))
