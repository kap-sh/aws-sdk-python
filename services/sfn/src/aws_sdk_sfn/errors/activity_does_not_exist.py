"""Generated from Smithy shape ``com.amazonaws.sfn#ActivityDoesNotExist``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.error_message


class ActivityDoesNotExist_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityDoesNotExist_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityDoesNotExist_:
    out: ActivityDoesNotExist_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ActivityDoesNotExist(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#ActivityDoesNotExist``."""

    code: str | None = "ActivityDoesNotExist"

    def __init__(self, data: ActivityDoesNotExist_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ActivityDoesNotExist",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ActivityDoesNotExist":
        return cls(deserialize_aws_json_1_0(data))
