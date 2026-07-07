"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ResourceAlreadyExistsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.exception_message
    import aws_sdk_database_migration_service.types.resource_arn


class ResourceAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_database_migration_service.types.exception_message.ExceptionMessage"
    ]
    """<p></p>"""
    resource_arn: NotRequired[
        "aws_sdk_database_migration_service.types.resource_arn.ResourceArn"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAlreadyExistsFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceAlreadyExistsFault_:
    out: ResourceAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    return out


class ResourceAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#ResourceAlreadyExistsFault``."""

    code: str | None = "ResourceAlreadyExistsFault"

    def __init__(self, data: ResourceAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceAlreadyExistsFault":
        return cls(deserialize_aws_json_1_1(data))
