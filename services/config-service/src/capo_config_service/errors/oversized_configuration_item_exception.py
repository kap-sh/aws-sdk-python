"""Generated from Smithy shape ``com.amazonaws.configservice#OversizedConfigurationItemException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.error_message


class OversizedConfigurationItemException_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OversizedConfigurationItemException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OversizedConfigurationItemException_:
    out: OversizedConfigurationItemException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class OversizedConfigurationItemException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#OversizedConfigurationItemException``."""

    code: str | None = "OversizedConfigurationItemException"

    def __init__(self, data: OversizedConfigurationItemException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OversizedConfigurationItemException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OversizedConfigurationItemException":
        return cls(deserialize_aws_json_1_1(data))
