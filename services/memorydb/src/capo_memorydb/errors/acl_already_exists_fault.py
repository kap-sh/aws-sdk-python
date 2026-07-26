"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLAlreadyExistsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import capo_memorydb.types.exception_message


class ACLAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["capo_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLAlreadyExistsFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ACLAlreadyExistsFault_:
    out: ACLAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ACLAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#ACLAlreadyExistsFault``."""

    code: str | None = "ACLAlreadyExistsFault"

    def __init__(self, data: ACLAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ACLAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ACLAlreadyExistsFault":
        return cls(deserialize_aws_json_1_1(data))
