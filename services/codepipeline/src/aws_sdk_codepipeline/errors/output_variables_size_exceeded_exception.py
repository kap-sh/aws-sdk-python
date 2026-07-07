"""Generated from Smithy shape ``com.amazonaws.codepipeline#OutputVariablesSizeExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.message


class OutputVariablesSizeExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codepipeline.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputVariablesSizeExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputVariablesSizeExceededException_:
    out: OutputVariablesSizeExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class OutputVariablesSizeExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#OutputVariablesSizeExceededException``."""

    code: str | None = "OutputVariablesSizeExceededException"

    def __init__(self, data: OutputVariablesSizeExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OutputVariablesSizeExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OutputVariablesSizeExceededException":
        return cls(deserialize_aws_json_1_1(data))
