"""Generated from Smithy shape ``com.amazonaws.fsx#IncompatibleParameterError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message
    import aws_sdk_fsx.types.parameter


class IncompatibleParameterError_(TypedDict):
    parameter: NotRequired["aws_sdk_fsx.types.parameter.Parameter"]
    """<p>A parameter that is incompatible with the earlier request.</p>"""
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncompatibleParameterError_) -> dict:
    out: dict = {}
    if "parameter" in value:
        out["Parameter"] = value["parameter"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IncompatibleParameterError_:
    out: IncompatibleParameterError_ = {}  # type: ignore[typeddict-item]
    if "Parameter" in data:
        out["parameter"] = data["Parameter"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IncompatibleParameterError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#IncompatibleParameterError``."""

    code: str | None = "IncompatibleParameterError"

    def __init__(self, data: IncompatibleParameterError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncompatibleParameterError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IncompatibleParameterError":
        return cls(deserialize_aws_json_1_1(data))
