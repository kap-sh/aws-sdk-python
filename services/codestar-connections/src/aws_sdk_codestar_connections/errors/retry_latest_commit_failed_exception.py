"""Generated from Smithy shape ``com.amazonaws.codestarconnections#RetryLatestCommitFailedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codestar_connections.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.error_message


class RetryLatestCommitFailedException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_codestar_connections.types.error_message.ErrorMessage"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RetryLatestCommitFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RetryLatestCommitFailedException_:
    out: RetryLatestCommitFailedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class RetryLatestCommitFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codestarconnections#RetryLatestCommitFailedException``."""

    code: str | None = "RetryLatestCommitFailedException"

    def __init__(self, data: RetryLatestCommitFailedException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="RetryLatestCommitFailedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "RetryLatestCommitFailedException":
        return cls(deserialize_aws_json_1_0(data))
