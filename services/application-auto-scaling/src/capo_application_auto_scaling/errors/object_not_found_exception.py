"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ObjectNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_auto_scaling.errors import ServiceError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.error_message


class ObjectNotFoundException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_application_auto_scaling.types.error_message.ErrorMessage"
    ]


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
    """Modeled error for Smithy shape ``com.amazonaws.applicationautoscaling#ObjectNotFoundException``."""

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
