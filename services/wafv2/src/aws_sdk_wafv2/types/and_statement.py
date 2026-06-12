"""Generated from Smithy shape ``com.amazonaws.wafv2#AndStatement``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.statements


class AndStatement(TypedDict):
    statements: "aws_sdk_wafv2.types.statements.Statements"
    """<p>The statements to combine with AND logic. You can use any statements that can be nested. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AndStatement) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.statements

    out["Statements"] = aws_sdk_wafv2.types.statements.serialize_aws_json_1_1(
        value["statements"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AndStatement:
    out: AndStatement = {}  # type: ignore[typeddict-item]
    if "Statements" in data:
        import aws_sdk_wafv2.types.statements

        out["statements"] = aws_sdk_wafv2.types.statements.deserialize_aws_json_1_1(
            data["Statements"]
        )
    else:
        raise DeserializationError("AndStatement.statements required")
    return out
