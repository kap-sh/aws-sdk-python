"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentAlreadyExists``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class DocumentAlreadyExists_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAlreadyExists_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentAlreadyExists_:
    out: DocumentAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DocumentAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#DocumentAlreadyExists``."""

    code: str | None = "DocumentAlreadyExists"

    def __init__(self, data: DocumentAlreadyExists_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DocumentAlreadyExists",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DocumentAlreadyExists":
        return cls(deserialize_aws_json_1_1(data))
