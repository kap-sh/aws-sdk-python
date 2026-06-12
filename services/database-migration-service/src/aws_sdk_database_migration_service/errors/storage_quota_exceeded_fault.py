"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StorageQuotaExceededFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.exception_message


class StorageQuotaExceededFault_(TypedDict):
    message: NotRequired[
        "aws_sdk_database_migration_service.types.exception_message.ExceptionMessage"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageQuotaExceededFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageQuotaExceededFault_:
    out: StorageQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class StorageQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#StorageQuotaExceededFault``."""

    code: str | None = "StorageQuotaExceededFault"

    def __init__(self, data: StorageQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="StorageQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "StorageQuotaExceededFault":
        return cls(deserialize_aws_json_1_1(data))
