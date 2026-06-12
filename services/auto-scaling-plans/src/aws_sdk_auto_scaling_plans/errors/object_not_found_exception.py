"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ObjectNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling_plans.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.error_message


class ObjectNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_auto_scaling_plans.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ObjectNotFoundException_:
    out: ObjectNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ObjectNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.autoscalingplans#ObjectNotFoundException``."""

    code: str | None = "ObjectNotFoundException"

    def __init__(self, data: ObjectNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ObjectNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ObjectNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
