"""Generated from Smithy shape ``com.amazonaws.memorydb#TestFailoverNotAvailableFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import capo_memorydb.types.exception_message


class TestFailoverNotAvailableFault_(TypedDict, closed=True):
    message: NotRequired["capo_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestFailoverNotAvailableFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestFailoverNotAvailableFault_:
    out: TestFailoverNotAvailableFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TestFailoverNotAvailableFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#TestFailoverNotAvailableFault``."""

    code: str | None = "TestFailoverNotAvailableFault"

    def __init__(self, data: TestFailoverNotAvailableFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TestFailoverNotAvailableFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TestFailoverNotAvailableFault":
        return cls(deserialize_aws_json_1_1(data))
