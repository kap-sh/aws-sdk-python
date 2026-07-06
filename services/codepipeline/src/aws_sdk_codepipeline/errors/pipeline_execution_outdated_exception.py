"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionOutdatedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.message


class PipelineExecutionOutdatedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codepipeline.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionOutdatedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionOutdatedException_:
    out: PipelineExecutionOutdatedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PipelineExecutionOutdatedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionOutdatedException``."""

    code: str | None = "PipelineExecutionOutdatedException"

    def __init__(self, data: PipelineExecutionOutdatedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PipelineExecutionOutdatedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PipelineExecutionOutdatedException":
        return cls(deserialize_aws_json_1_1(data))
