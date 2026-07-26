"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionNotRedrivable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import ServiceError

if TYPE_CHECKING:
    import capo_sfn.types.error_message


class ExecutionNotRedrivable_(TypedDict, closed=True):
    message: NotRequired["capo_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionNotRedrivable_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionNotRedrivable_:
    out: ExecutionNotRedrivable_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ExecutionNotRedrivable(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#ExecutionNotRedrivable``."""

    code: str | None = "ExecutionNotRedrivable"

    def __init__(self, data: ExecutionNotRedrivable_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExecutionNotRedrivable",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ExecutionNotRedrivable":
        return cls(deserialize_aws_json_1_0(data))
