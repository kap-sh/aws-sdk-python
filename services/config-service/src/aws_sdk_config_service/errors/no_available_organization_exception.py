"""Generated from Smithy shape ``com.amazonaws.configservice#NoAvailableOrganizationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.error_message


class NoAvailableOrganizationException_(TypedDict):
    message: NotRequired["aws_sdk_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoAvailableOrganizationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoAvailableOrganizationException_:
    out: NoAvailableOrganizationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NoAvailableOrganizationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#NoAvailableOrganizationException``."""

    code: str | None = "NoAvailableOrganizationException"

    def __init__(self, data: NoAvailableOrganizationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoAvailableOrganizationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NoAvailableOrganizationException":
        return cls(deserialize_aws_json_1_1(data))
