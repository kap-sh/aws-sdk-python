"""Generated from Smithy shape ``com.amazonaws.configservice#NoSuchOrganizationConfigRuleException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.error_message


class NoSuchOrganizationConfigRuleException_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoSuchOrganizationConfigRuleException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoSuchOrganizationConfigRuleException_:
    out: NoSuchOrganizationConfigRuleException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NoSuchOrganizationConfigRuleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#NoSuchOrganizationConfigRuleException``."""

    code: str | None = "NoSuchOrganizationConfigRuleException"

    def __init__(self, data: NoSuchOrganizationConfigRuleException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchOrganizationConfigRuleException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NoSuchOrganizationConfigRuleException":
        return cls(deserialize_aws_json_1_1(data))
