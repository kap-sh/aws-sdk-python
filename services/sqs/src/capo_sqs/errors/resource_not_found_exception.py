"""Generated from Smithy shape ``com.amazonaws.sqs#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import ServiceError

if TYPE_CHECKING:
    import capo_sqs.types.exception_message


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_0(data), message)
