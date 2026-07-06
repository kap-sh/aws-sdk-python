"""Generated from Smithy shape ``com.amazonaws.migrationhub#HomeRegionNotSetException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_migration_hub.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.error_message


class HomeRegionNotSetException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_migration_hub.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HomeRegionNotSetException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HomeRegionNotSetException_:
    out: HomeRegionNotSetException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class HomeRegionNotSetException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhub#HomeRegionNotSetException``."""

    code: str | None = "HomeRegionNotSetException"

    def __init__(self, data: HomeRegionNotSetException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="HomeRegionNotSetException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "HomeRegionNotSetException":
        return cls(deserialize_aws_json_1_1(data))
