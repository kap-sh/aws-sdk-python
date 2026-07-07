"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionNotStoppableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.message


class PipelineExecutionNotStoppableException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codepipeline.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionNotStoppableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionNotStoppableException_:
    out: PipelineExecutionNotStoppableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PipelineExecutionNotStoppableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionNotStoppableException``."""

    code: str | None = "PipelineExecutionNotStoppableException"

    def __init__(self, data: PipelineExecutionNotStoppableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PipelineExecutionNotStoppableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PipelineExecutionNotStoppableException":
        return cls(deserialize_aws_json_1_1(data))
