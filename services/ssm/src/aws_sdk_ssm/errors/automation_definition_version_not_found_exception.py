"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationDefinitionVersionNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class AutomationDefinitionVersionNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AutomationDefinitionVersionNotFoundException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AutomationDefinitionVersionNotFoundException_:
    out: AutomationDefinitionVersionNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AutomationDefinitionVersionNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#AutomationDefinitionVersionNotFoundException``."""

    code: str | None = "AutomationDefinitionVersionNotFoundException"

    def __init__(self, data: AutomationDefinitionVersionNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AutomationDefinitionVersionNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "AutomationDefinitionVersionNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
