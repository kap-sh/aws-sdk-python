"""Generated from Smithy shape ``com.amazonaws.athena#GetPreparedStatementOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.prepared_statement


class GetPreparedStatementOutput(TypedDict, closed=True):
    prepared_statement: NotRequired[
        "aws_sdk_athena.types.prepared_statement.PreparedStatement"
    ]
    """<p>The name of the prepared statement that was retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPreparedStatementOutput) -> dict:
    out: dict = {}
    if "prepared_statement" in value:
        import aws_sdk_athena.types.prepared_statement

        out["PreparedStatement"] = (
            aws_sdk_athena.types.prepared_statement.serialize_aws_json_1_1(
                value["prepared_statement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPreparedStatementOutput:
    out: GetPreparedStatementOutput = {}  # type: ignore[typeddict-item]
    if "PreparedStatement" in data:
        import aws_sdk_athena.types.prepared_statement

        out["prepared_statement"] = (
            aws_sdk_athena.types.prepared_statement.deserialize_aws_json_1_1(
                data["PreparedStatement"]
            )
        )
    return out
