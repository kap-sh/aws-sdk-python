"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConcurrentPipelineExecutionsLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.message


class ConcurrentPipelineExecutionsLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_codepipeline.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ConcurrentPipelineExecutionsLimitExceededException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ConcurrentPipelineExecutionsLimitExceededException_:
    out: ConcurrentPipelineExecutionsLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ConcurrentPipelineExecutionsLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#ConcurrentPipelineExecutionsLimitExceededException``."""

    code: str | None = "ConcurrentPipelineExecutionsLimitExceededException"

    def __init__(self, data: ConcurrentPipelineExecutionsLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentPipelineExecutionsLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "ConcurrentPipelineExecutionsLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
