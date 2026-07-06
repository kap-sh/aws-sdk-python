"""Generated from Smithy shape ``com.amazonaws.ecs#AttributeLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class AttributeLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeLimitExceededException_:
    out: AttributeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AttributeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#AttributeLimitExceededException``."""

    code: str | None = "AttributeLimitExceededException"

    def __init__(self, data: AttributeLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AttributeLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AttributeLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
