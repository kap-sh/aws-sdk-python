"""Generated from Smithy shape ``com.amazonaws.glue#GlueEncryptionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class GlueEncryptionException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>The message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueEncryptionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GlueEncryptionException_:
    out: GlueEncryptionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class GlueEncryptionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#GlueEncryptionException``."""

    code: str | None = "GlueEncryptionException"

    def __init__(self, data: GlueEncryptionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GlueEncryptionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "GlueEncryptionException":
        return cls(deserialize_aws_json_1_1(data))
