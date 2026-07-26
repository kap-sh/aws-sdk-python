"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ExecuteStatementException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_data.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_redshift_data.types.string


class ExecuteStatementException_(TypedDict, closed=True):
    message: "capo_redshift_data.types.string.String"
    """<p>The exception message.</p>"""
    statement_id: "capo_redshift_data.types.string.String"
    """<p>Statement identifier of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteStatementException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["StatementId"] = value["statement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteStatementException_:
    out: ExecuteStatementException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ExecuteStatementException_.message required")
    if "StatementId" in data:
        out["statement_id"] = data["StatementId"]
    else:
        raise DeserializationError("ExecuteStatementException_.statement_id required")
    return out


class ExecuteStatementException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftdata#ExecuteStatementException``."""

    code: str | None = "ExecuteStatementException"

    def __init__(self, data: ExecuteStatementException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ExecuteStatementException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ExecuteStatementException":
        return cls(deserialize_aws_json_1_1(data))
