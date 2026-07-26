"""Generated from Smithy shape ``com.amazonaws.gamelift#IdempotentParameterMismatchException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string


class IdempotentParameterMismatchException_(TypedDict, closed=True):
    message: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdempotentParameterMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdempotentParameterMismatchException_:
    out: IdempotentParameterMismatchException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IdempotentParameterMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#IdempotentParameterMismatchException``."""

    code: str | None = "IdempotentParameterMismatchException"

    def __init__(self, data: IdempotentParameterMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotentParameterMismatchException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IdempotentParameterMismatchException":
        return cls(deserialize_aws_json_1_1(data))
