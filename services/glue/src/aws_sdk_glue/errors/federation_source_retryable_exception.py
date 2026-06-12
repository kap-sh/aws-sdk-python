"""Generated from Smithy shape ``com.amazonaws.glue#FederationSourceRetryableException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class FederationSourceRetryableException_(TypedDict):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederationSourceRetryableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FederationSourceRetryableException_:
    out: FederationSourceRetryableException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FederationSourceRetryableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#FederationSourceRetryableException``."""

    code: str | None = "FederationSourceRetryableException"

    def __init__(self, data: FederationSourceRetryableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FederationSourceRetryableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FederationSourceRetryableException":
        return cls(deserialize_aws_json_1_1(data))
