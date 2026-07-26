"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KMSAccessDeniedFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_database_migration_service.types.exception_message


class KMSAccessDeniedFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_database_migration_service.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSAccessDeniedFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSAccessDeniedFault_:
    out: KMSAccessDeniedFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KMSAccessDeniedFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#KMSAccessDeniedFault``."""

    code: str | None = "KMSAccessDeniedFault"

    def __init__(self, data: KMSAccessDeniedFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSAccessDeniedFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KMSAccessDeniedFault":
        return cls(deserialize_aws_json_1_1(data))
