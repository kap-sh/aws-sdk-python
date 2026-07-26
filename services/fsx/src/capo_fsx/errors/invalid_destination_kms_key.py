"""Generated from Smithy shape ``com.amazonaws.fsx#InvalidDestinationKmsKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class InvalidDestinationKmsKey_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidDestinationKmsKey_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidDestinationKmsKey_:
    out: InvalidDestinationKmsKey_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidDestinationKmsKey(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#InvalidDestinationKmsKey``."""

    code: str | None = "InvalidDestinationKmsKey"

    def __init__(self, data: InvalidDestinationKmsKey_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDestinationKmsKey",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidDestinationKmsKey":
        return cls(deserialize_aws_json_1_1(data))
