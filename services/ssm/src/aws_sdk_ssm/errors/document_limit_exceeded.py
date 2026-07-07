"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentLimitExceeded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class DocumentLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentLimitExceeded_:
    out: DocumentLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DocumentLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#DocumentLimitExceeded``."""

    code: str | None = "DocumentLimitExceeded"

    def __init__(self, data: DocumentLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DocumentLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DocumentLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
