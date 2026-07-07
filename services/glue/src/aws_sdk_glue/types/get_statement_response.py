"""Generated from Smithy shape ``com.amazonaws.glue#GetStatementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.statement


class GetStatementResponse(TypedDict, closed=True):
    statement: NotRequired["aws_sdk_glue.types.statement.Statement"]
    """<p>Returns the statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStatementResponse) -> dict:
    out: dict = {}
    if "statement" in value:
        import aws_sdk_glue.types.statement

        out["Statement"] = aws_sdk_glue.types.statement.serialize_aws_json_1_1(
            value["statement"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStatementResponse:
    out: GetStatementResponse = {}  # type: ignore[typeddict-item]
    if "Statement" in data:
        import aws_sdk_glue.types.statement

        out["statement"] = aws_sdk_glue.types.statement.deserialize_aws_json_1_1(
            data["Statement"]
        )
    return out
