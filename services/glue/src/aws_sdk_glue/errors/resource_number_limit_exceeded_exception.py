"""Generated from Smithy shape ``com.amazonaws.glue#ResourceNumberLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class ResourceNumberLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNumberLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNumberLimitExceededException_:
    out: ResourceNumberLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceNumberLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#ResourceNumberLimitExceededException``."""

    code: str | None = "ResourceNumberLimitExceededException"

    def __init__(self, data: ResourceNumberLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNumberLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceNumberLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
