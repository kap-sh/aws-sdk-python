"""Generated from Smithy shape ``com.amazonaws.configservice#NoSuchConfigRuleInConformancePackException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.error_message


class NoSuchConfigRuleInConformancePackException_(TypedDict):
    message: NotRequired["aws_sdk_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoSuchConfigRuleInConformancePackException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoSuchConfigRuleInConformancePackException_:
    out: NoSuchConfigRuleInConformancePackException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NoSuchConfigRuleInConformancePackException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#NoSuchConfigRuleInConformancePackException``."""

    code: str | None = "NoSuchConfigRuleInConformancePackException"

    def __init__(self, data: NoSuchConfigRuleInConformancePackException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchConfigRuleInConformancePackException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "NoSuchConfigRuleInConformancePackException":
        return cls(deserialize_aws_json_1_1(data))
