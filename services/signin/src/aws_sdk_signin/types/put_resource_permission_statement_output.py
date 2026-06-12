"""Generated from Smithy shape ``com.amazonaws.signin#PutResourcePermissionStatementOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_signin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signin.types.statement_id


class PutResourcePermissionStatementOutput(TypedDict):
    statement_id: "aws_sdk_signin.types.statement_id.StatementId"
    """Unique identifier for the created permission statement"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePermissionStatementOutput) -> dict:
    out: dict = {}
    out["statementId"] = value["statement_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePermissionStatementOutput:
    out: PutResourcePermissionStatementOutput = {}  # type: ignore[typeddict-item]
    if "statementId" in data:
        out["statement_id"] = data["statementId"]
    else:
        raise DeserializationError(
            "PutResourcePermissionStatementOutput.statement_id required"
        )
    return out
