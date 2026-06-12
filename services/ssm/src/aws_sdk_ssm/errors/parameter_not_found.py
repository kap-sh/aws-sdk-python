"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterNotFound``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class ParameterNotFound_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterNotFound_:
    out: ParameterNotFound_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ParameterNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ParameterNotFound``."""

    code: str | None = "ParameterNotFound"

    def __init__(self, data: ParameterNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ParameterNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ParameterNotFound":
        return cls(deserialize_aws_json_1_1(data))
