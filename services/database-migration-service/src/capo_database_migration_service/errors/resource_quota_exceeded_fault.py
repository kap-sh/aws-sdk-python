"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ResourceQuotaExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_database_migration_service.types.exception_message


class ResourceQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_database_migration_service.types.exception_message.ExceptionMessage"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceQuotaExceededFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceQuotaExceededFault_:
    out: ResourceQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#ResourceQuotaExceededFault``."""

    code: str | None = "ResourceQuotaExceededFault"

    def __init__(self, data: ResourceQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceQuotaExceededFault":
        return cls(deserialize_aws_json_1_1(data))
