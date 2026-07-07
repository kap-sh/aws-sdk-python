"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidInstancePropertyFilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidInstancePropertyFilterValue_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInstancePropertyFilterValue_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInstancePropertyFilterValue_:
    out: InvalidInstancePropertyFilterValue_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidInstancePropertyFilterValue(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidInstancePropertyFilterValue``."""

    code: str | None = "InvalidInstancePropertyFilterValue"

    def __init__(self, data: InvalidInstancePropertyFilterValue_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInstancePropertyFilterValue",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidInstancePropertyFilterValue":
        return cls(deserialize_aws_json_1_1(data))
