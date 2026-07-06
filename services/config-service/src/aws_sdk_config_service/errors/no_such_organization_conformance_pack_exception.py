"""Generated from Smithy shape ``com.amazonaws.configservice#NoSuchOrganizationConformancePackException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.error_message


class NoSuchOrganizationConformancePackException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoSuchOrganizationConformancePackException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoSuchOrganizationConformancePackException_:
    out: NoSuchOrganizationConformancePackException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NoSuchOrganizationConformancePackException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#NoSuchOrganizationConformancePackException``."""

    code: str | None = "NoSuchOrganizationConformancePackException"

    def __init__(self, data: NoSuchOrganizationConformancePackException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchOrganizationConformancePackException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "NoSuchOrganizationConformancePackException":
        return cls(deserialize_aws_json_1_1(data))
