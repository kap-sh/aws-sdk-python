"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#S3AccessDeniedFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.exception_message


class S3AccessDeniedFault_(TypedDict):
    message: NotRequired[
        "aws_sdk_database_migration_service.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessDeniedFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3AccessDeniedFault_:
    out: S3AccessDeniedFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class S3AccessDeniedFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#S3AccessDeniedFault``."""

    code: str | None = "S3AccessDeniedFault"

    def __init__(self, data: S3AccessDeniedFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="S3AccessDeniedFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "S3AccessDeniedFault":
        return cls(deserialize_aws_json_1_1(data))
