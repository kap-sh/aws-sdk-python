"""Generated from Smithy shape ``com.amazonaws.signin#PermissionStatementSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_signin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signin.types.condition_block
    import aws_sdk_signin.types.statement_id


class PermissionStatementSummary(TypedDict, closed=True):
    sid: "aws_sdk_signin.types.statement_id.StatementId"
    """Unique identifier for the permission statement"""
    condition: NotRequired["aws_sdk_signin.types.condition_block.ConditionBlock"]
    """Condition block for the permission statement"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionStatementSummary) -> dict:
    out: dict = {}
    out["sid"] = value["sid"]
    if "condition" in value:
        import aws_sdk_signin.types.condition_block

        out["condition"] = aws_sdk_signin.types.condition_block.serialize_json(
            value["condition"]
        )
    return out


def deserialize_json(data: dict) -> PermissionStatementSummary:
    out: PermissionStatementSummary = {}  # type: ignore[typeddict-item]
    if "sid" in data:
        out["sid"] = data["sid"]
    else:
        raise DeserializationError("PermissionStatementSummary.sid required")
    if "condition" in data:
        import aws_sdk_signin.types.condition_block

        out["condition"] = aws_sdk_signin.types.condition_block.deserialize_json(
            data["condition"]
        )
    return out
