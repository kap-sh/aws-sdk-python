"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KMSKeyNotAccessibleFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.exception_message


class KMSKeyNotAccessibleFault_(TypedDict):
    message: NotRequired[
        "aws_sdk_database_migration_service.types.exception_message.ExceptionMessage"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSKeyNotAccessibleFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSKeyNotAccessibleFault_:
    out: KMSKeyNotAccessibleFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KMSKeyNotAccessibleFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#KMSKeyNotAccessibleFault``."""

    code: str | None = "KMSKeyNotAccessibleFault"

    def __init__(self, data: KMSKeyNotAccessibleFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSKeyNotAccessibleFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KMSKeyNotAccessibleFault":
        return cls(deserialize_aws_json_1_1(data))
