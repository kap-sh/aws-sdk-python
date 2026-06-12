"""Generated from Smithy shape ``com.amazonaws.licensemanager#FilterLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.message


class FilterLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterLimitExceededException_:
    out: FilterLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FilterLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#FilterLimitExceededException``."""

    code: str | None = "FilterLimitExceededException"

    def __init__(self, data: FilterLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FilterLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FilterLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
