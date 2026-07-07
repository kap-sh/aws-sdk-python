"""Generated from Smithy shape ``com.amazonaws.licensemanager#EntitlementNotAllowedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.message


class EntitlementNotAllowedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementNotAllowedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitlementNotAllowedException_:
    out: EntitlementNotAllowedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EntitlementNotAllowedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#EntitlementNotAllowedException``."""

    code: str | None = "EntitlementNotAllowedException"

    def __init__(self, data: EntitlementNotAllowedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntitlementNotAllowedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EntitlementNotAllowedException":
        return cls(deserialize_aws_json_1_1(data))
