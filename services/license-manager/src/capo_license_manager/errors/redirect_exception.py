"""Generated from Smithy shape ``com.amazonaws.licensemanager#RedirectException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_license_manager.types.location
    import capo_license_manager.types.message


class RedirectException_(TypedDict, closed=True):
    location: NotRequired["capo_license_manager.types.location.Location"]
    message: NotRequired["capo_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedirectException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedirectException_:
    out: RedirectException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class RedirectException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#RedirectException``."""

    code: str | None = "RedirectException"

    def __init__(self, data: RedirectException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RedirectException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RedirectException":
        return cls(deserialize_aws_json_1_1(data))
