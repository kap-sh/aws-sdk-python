"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KMSFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.exception_message


class KMSFault_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_database_migration_service.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSFault_:
    out: KMSFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KMSFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#KMSFault``."""

    code: str | None = "KMSFault"

    def __init__(self, data: KMSFault_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="KMSFault"
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KMSFault":
        return cls(deserialize_aws_json_1_1(data))
