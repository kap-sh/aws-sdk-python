"""Generated from Smithy shape ``com.amazonaws.ssm#TooManyUpdates``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class TooManyUpdates_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyUpdates_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyUpdates_:
    out: TooManyUpdates_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TooManyUpdates(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#TooManyUpdates``."""

    code: str | None = "TooManyUpdates"

    def __init__(self, data: TooManyUpdates_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyUpdates",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TooManyUpdates":
        return cls(deserialize_aws_json_1_1(data))
