"""Generated from Smithy shape ``com.amazonaws.rdsdata#StatementTimeoutException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.error_message
    import aws_sdk_rds_data.types.long


class StatementTimeoutException_(TypedDict):
    message: NotRequired["aws_sdk_rds_data.types.error_message.ErrorMessage"]
    """<p>The error message returned by this <code>StatementTimeoutException</code> error.</p>"""
    db_connection_id: "aws_sdk_rds_data.types.long.Long"
    """<p>The database connection ID that executed the SQL statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatementTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["dbConnectionId"] = value.get("db_connection_id", 0)
    return out


def deserialize_json(data: dict) -> StatementTimeoutException_:
    out: StatementTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "dbConnectionId" in data:
        out["db_connection_id"] = data["dbConnectionId"]
    else:
        out["db_connection_id"] = 0
    return out


class StatementTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#StatementTimeoutException``."""

    code: str | None = "StatementTimeoutException"

    def __init__(self, data: StatementTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="StatementTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "StatementTimeoutException":
        return cls(deserialize_json(data))
