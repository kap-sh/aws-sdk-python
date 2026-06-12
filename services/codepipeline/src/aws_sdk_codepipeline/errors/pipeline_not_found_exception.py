"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.message


class PipelineNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_codepipeline.types.message.Message"]
    """<p>The message provided to the user in the event of an exception.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#PipelineNotFoundException``."""

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
