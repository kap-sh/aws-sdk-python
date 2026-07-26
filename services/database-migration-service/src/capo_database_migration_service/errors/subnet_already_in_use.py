"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SubnetAlreadyInUse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_database_migration_service.types.exception_message


class SubnetAlreadyInUse_(TypedDict, closed=True):
    message: NotRequired[
        "capo_database_migration_service.types.exception_message.ExceptionMessage"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetAlreadyInUse_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubnetAlreadyInUse_:
    out: SubnetAlreadyInUse_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SubnetAlreadyInUse(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.databasemigrationservice#SubnetAlreadyInUse``."""

    code: str | None = "SubnetAlreadyInUse"

    def __init__(self, data: SubnetAlreadyInUse_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SubnetAlreadyInUse",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SubnetAlreadyInUse":
        return cls(deserialize_aws_json_1_1(data))
