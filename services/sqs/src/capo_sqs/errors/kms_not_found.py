"""Generated from Smithy shape ``com.amazonaws.sqs#KmsNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import ServiceError

if TYPE_CHECKING:
    import capo_sqs.types.exception_message


class KmsNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsNotFound_:
    out: KmsNotFound_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KmsNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#KmsNotFound``."""

    code: str | None = "KmsNotFound"

    def __init__(self, data: KmsNotFound_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="KmsNotFound"
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "KmsNotFound":
        return cls(deserialize_aws_json_1_0(data))
