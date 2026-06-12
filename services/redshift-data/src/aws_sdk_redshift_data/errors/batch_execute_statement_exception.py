"""Generated from Smithy shape ``com.amazonaws.redshiftdata#BatchExecuteStatementException``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_redshift_data.errors import DeserializationError
from aws_sdk_redshift_data.errors import ServiceError
if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.string

class BatchExecuteStatementException_(TypedDict):
    message: "aws_sdk_redshift_data.types.string.String"
    statement_id: "aws_sdk_redshift_data.types.string.String"
    """<p>Statement identifier of the exception.</p>"""

# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchExecuteStatementException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["StatementId"] = value["statement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchExecuteStatementException_:
    out: BatchExecuteStatementException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("BatchExecuteStatementException_.message required")
    if "StatementId" in data:
        out["statement_id"] = data["StatementId"]
    else:
        raise DeserializationError("BatchExecuteStatementException_.statement_id required")
    return out


class BatchExecuteStatementException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftdata#BatchExecuteStatementException``."""
    code: str | None = 'BatchExecuteStatementException'

    def __init__(self, data: BatchExecuteStatementException_):
        super().__init__('server', is_throttling_error=False, is_retryable=False, code='BatchExecuteStatementException')
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BatchExecuteStatementException":
        return cls(deserialize_aws_json_1_1(data))