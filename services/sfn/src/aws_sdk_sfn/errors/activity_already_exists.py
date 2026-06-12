"""Generated from Smithy shape ``com.amazonaws.sfn#ActivityAlreadyExists``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.error_message


class ActivityAlreadyExists_(TypedDict):
    message: NotRequired["aws_sdk_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityAlreadyExists_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityAlreadyExists_:
    out: ActivityAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ActivityAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#ActivityAlreadyExists``."""

    code: str | None = "ActivityAlreadyExists"

    def __init__(self, data: ActivityAlreadyExists_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ActivityAlreadyExists",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ActivityAlreadyExists":
        return cls(deserialize_aws_json_1_0(data))
