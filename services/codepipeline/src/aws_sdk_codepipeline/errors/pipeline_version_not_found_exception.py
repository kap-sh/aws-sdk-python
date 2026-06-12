"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineVersionNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.message


class PipelineVersionNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_codepipeline.types.message.Message"]
    """<p>The message provided to the user in the event of an exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVersionNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineVersionNotFoundException_:
    out: PipelineVersionNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PipelineVersionNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#PipelineVersionNotFoundException``."""

    code: str | None = "PipelineVersionNotFoundException"

    def __init__(self, data: PipelineVersionNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PipelineVersionNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PipelineVersionNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
