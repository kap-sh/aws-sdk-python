"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionNotOverridableException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.string


class ConditionNotOverridableException_(TypedDict):
    message: NotRequired["aws_sdk_codepipeline.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionNotOverridableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionNotOverridableException_:
    out: ConditionNotOverridableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ConditionNotOverridableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#ConditionNotOverridableException``."""

    code: str | None = "ConditionNotOverridableException"

    def __init__(self, data: ConditionNotOverridableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConditionNotOverridableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ConditionNotOverridableException":
        return cls(deserialize_aws_json_1_1(data))
