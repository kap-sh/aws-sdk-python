"""Generated from Smithy shape ``com.amazonaws.datapipeline#PipelineNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_data_pipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.error_message


class PipelineNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_data_pipeline.types.error_message.errorMessage"]
    """<p>Description of the error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineNotFoundException_:
    out: PipelineNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PipelineNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.datapipeline#PipelineNotFoundException``."""

    code: str | None = "PipelineNotFoundException"

    def __init__(self, data: PipelineNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PipelineNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PipelineNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
