"""Generated from Smithy shape ``com.amazonaws.redshiftdata#DatabaseConnectionException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_redshift_data.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.string


class DatabaseConnectionException_(TypedDict, closed=True):
    message: "aws_sdk_redshift_data.types.string.String"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseConnectionException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseConnectionException_:
    out: DatabaseConnectionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("DatabaseConnectionException_.message required")
    return out


class DatabaseConnectionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftdata#DatabaseConnectionException``."""

    code: str | None = "DatabaseConnectionException"

    def __init__(self, data: DatabaseConnectionException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DatabaseConnectionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DatabaseConnectionException":
        return cls(deserialize_aws_json_1_1(data))
