"""Generated from Smithy shape ``com.amazonaws.configservice#MaxNumberOfOrganizationConformancePacksExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.error_message


class MaxNumberOfOrganizationConformancePacksExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: MaxNumberOfOrganizationConformancePacksExceededException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> MaxNumberOfOrganizationConformancePacksExceededException_:
    out: MaxNumberOfOrganizationConformancePacksExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MaxNumberOfOrganizationConformancePacksExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#MaxNumberOfOrganizationConformancePacksExceededException``."""

    code: str | None = "MaxNumberOfOrganizationConformancePacksExceededException"

    def __init__(self, data: MaxNumberOfOrganizationConformancePacksExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MaxNumberOfOrganizationConformancePacksExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "MaxNumberOfOrganizationConformancePacksExceededException":
        return cls(deserialize_aws_json_1_1(data))
