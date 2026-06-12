"""Generated from Smithy shape ``com.amazonaws.configservice#MaxNumberOfConfigRulesExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.error_message


class MaxNumberOfConfigRulesExceededException_(TypedDict):
    message: NotRequired["aws_sdk_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaxNumberOfConfigRulesExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MaxNumberOfConfigRulesExceededException_:
    out: MaxNumberOfConfigRulesExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MaxNumberOfConfigRulesExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#MaxNumberOfConfigRulesExceededException``."""

    code: str | None = "MaxNumberOfConfigRulesExceededException"

    def __init__(self, data: MaxNumberOfConfigRulesExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MaxNumberOfConfigRulesExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MaxNumberOfConfigRulesExceededException":
        return cls(deserialize_aws_json_1_1(data))
