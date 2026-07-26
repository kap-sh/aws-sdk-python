"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationAccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.error_message


class OrganizationAccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationAccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationAccessDeniedException_:
    out: OrganizationAccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class OrganizationAccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#OrganizationAccessDeniedException``."""

    code: str | None = "OrganizationAccessDeniedException"

    def __init__(self, data: OrganizationAccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OrganizationAccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OrganizationAccessDeniedException":
        return cls(deserialize_aws_json_1_1(data))
