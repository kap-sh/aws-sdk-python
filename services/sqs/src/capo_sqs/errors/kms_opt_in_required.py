"""Generated from Smithy shape ``com.amazonaws.sqs#KmsOptInRequired``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import ServiceError

if TYPE_CHECKING:
    import capo_sqs.types.exception_message


class KmsOptInRequired_(TypedDict, closed=True):
    message: NotRequired["capo_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsOptInRequired_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsOptInRequired_:
    out: KmsOptInRequired_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KmsOptInRequired(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#KmsOptInRequired``."""

    code: str | None = "KmsOptInRequired"

    def __init__(self, data: KmsOptInRequired_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsOptInRequired",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "KmsOptInRequired":
        return cls(deserialize_aws_json_1_0(data))
