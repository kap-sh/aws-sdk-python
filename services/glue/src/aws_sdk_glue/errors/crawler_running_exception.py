"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerRunningException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class CrawlerRunningException_(TypedDict):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerRunningException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CrawlerRunningException_:
    out: CrawlerRunningException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CrawlerRunningException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#CrawlerRunningException``."""

    code: str | None = "CrawlerRunningException"

    def __init__(self, data: CrawlerRunningException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CrawlerRunningException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CrawlerRunningException":
        return cls(deserialize_aws_json_1_1(data))
