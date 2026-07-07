"""Generated from Smithy shape ``com.amazonaws.memorydb#InvalidParameterCombinationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.aws_query_error_message


class InvalidParameterCombinationException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_memorydb.types.aws_query_error_message.AwsQueryErrorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParameterCombinationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParameterCombinationException_:
    out: InvalidParameterCombinationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidParameterCombinationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#InvalidParameterCombinationException``."""

    code: str | None = "InvalidParameterCombinationException"

    def __init__(self, data: InvalidParameterCombinationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterCombinationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidParameterCombinationException":
        return cls(deserialize_aws_json_1_1(data))
