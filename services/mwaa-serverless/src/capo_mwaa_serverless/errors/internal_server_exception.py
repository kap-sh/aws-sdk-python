"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mwaa_serverless.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.error_message


class InternalServerException_(TypedDict, closed=True):
    message: "capo_mwaa_serverless.types.error_message.ErrorMessage"
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying the operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mwaaserverless#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_0(data))
