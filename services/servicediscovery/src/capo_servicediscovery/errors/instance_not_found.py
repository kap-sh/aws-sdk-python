"""Generated from Smithy shape ``com.amazonaws.servicediscovery#InstanceNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import capo_servicediscovery.types.error_message


class InstanceNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_servicediscovery.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceNotFound_:
    out: InstanceNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InstanceNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#InstanceNotFound``."""

    code: str | None = "InstanceNotFound"

    def __init__(self, data: InstanceNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InstanceNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InstanceNotFound":
        return cls(deserialize_aws_json_1_1(data))
