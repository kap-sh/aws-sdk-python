"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InvalidInsightSelectorsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class InvalidInsightSelectorsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInsightSelectorsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInsightSelectorsException_:
    out: InvalidInsightSelectorsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidInsightSelectorsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InvalidInsightSelectorsException``."""

    code: str | None = "InvalidInsightSelectorsException"

    def __init__(self, data: InvalidInsightSelectorsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInsightSelectorsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidInsightSelectorsException":
        return cls(deserialize_aws_json_1_1(data))
