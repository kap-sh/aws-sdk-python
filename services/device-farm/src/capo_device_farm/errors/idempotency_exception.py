"""Generated from Smithy shape ``com.amazonaws.devicefarm#IdempotencyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import ServiceError

if TYPE_CHECKING:
    import capo_device_farm.types.message


class IdempotencyException_(TypedDict, closed=True):
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>Any additional information about the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdempotencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdempotencyException_:
    out: IdempotencyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class IdempotencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devicefarm#IdempotencyException``."""

    code: str | None = "IdempotencyException"

    def __init__(self, data: IdempotencyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotencyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IdempotencyException":
        return cls(deserialize_aws_json_1_1(data))
