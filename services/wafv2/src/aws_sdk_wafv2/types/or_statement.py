"""Generated from Smithy shape ``com.amazonaws.wafv2#OrStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.statements


class OrStatement(TypedDict, closed=True):
    statements: "aws_sdk_wafv2.types.statements.Statements"
    """<p>The statements to combine with OR logic. You can use any statements that can be nested.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrStatement) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.statements

    out["Statements"] = aws_sdk_wafv2.types.statements.serialize_aws_json_1_1(
        value["statements"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrStatement:
    out: OrStatement = {}  # type: ignore[typeddict-item]
    if "Statements" in data:
        import aws_sdk_wafv2.types.statements

        out["statements"] = aws_sdk_wafv2.types.statements.deserialize_aws_json_1_1(
            data["Statements"]
        )
    else:
        raise DeserializationError("OrStatement.statements required")
    return out
