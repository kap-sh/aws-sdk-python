"""Generated from Smithy shape ``com.amazonaws.codepipeline#UnableToRollbackStageException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import capo_codepipeline.types.string


class UnableToRollbackStageException_(TypedDict, closed=True):
    message: NotRequired["capo_codepipeline.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnableToRollbackStageException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnableToRollbackStageException_:
    out: UnableToRollbackStageException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnableToRollbackStageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#UnableToRollbackStageException``."""

    code: str | None = "UnableToRollbackStageException"

    def __init__(self, data: UnableToRollbackStageException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnableToRollbackStageException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnableToRollbackStageException":
        return cls(deserialize_aws_json_1_1(data))
