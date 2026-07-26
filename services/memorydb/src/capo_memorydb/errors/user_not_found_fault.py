"""Generated from Smithy shape ``com.amazonaws.memorydb#UserNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import capo_memorydb.types.exception_message


class UserNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserNotFoundFault_:
    out: UserNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UserNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#UserNotFoundFault``."""

    code: str | None = "UserNotFoundFault"

    def __init__(self, data: UserNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UserNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UserNotFoundFault":
        return cls(deserialize_aws_json_1_1(data))
