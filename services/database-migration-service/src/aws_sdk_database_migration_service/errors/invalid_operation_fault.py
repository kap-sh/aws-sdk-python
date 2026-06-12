"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#InvalidOperationFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.exception_message


class InvalidOperationFault_(TypedDict):
    message: NotRequired[
        "aws_sdk_database_migration_service.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidOperationFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidOperationFault_:
    out: InvalidOperationFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidOperationFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#InvalidOperationFault``."""

    code: str | None = "InvalidOperationFault"

    def __init__(self, data: InvalidOperationFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidOperationFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidOperationFault":
        return cls(deserialize_aws_json_1_1(data))
