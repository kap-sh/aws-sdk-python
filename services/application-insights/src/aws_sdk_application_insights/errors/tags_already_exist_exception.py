"""Generated from Smithy shape ``com.amazonaws.applicationinsights#TagsAlreadyExistException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_insights.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.exception_message


class TagsAlreadyExistException_(TypedDict):
    message: NotRequired[
        "aws_sdk_application_insights.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagsAlreadyExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagsAlreadyExistException_:
    out: TagsAlreadyExistException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TagsAlreadyExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationinsights#TagsAlreadyExistException``."""

    code: str | None = "TagsAlreadyExistException"

    def __init__(self, data: TagsAlreadyExistException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagsAlreadyExistException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TagsAlreadyExistException":
        return cls(deserialize_aws_json_1_1(data))
