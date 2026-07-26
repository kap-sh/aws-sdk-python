"""Generated from Smithy shape ``com.amazonaws.wafv2#NotStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.statement


class NotStatement(TypedDict, closed=True):
    statement: "capo_wafv2.types.statement.Statement"
    """<p>The statement to negate. You can use any statement that can be nested.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotStatement) -> dict:
    out: dict = {}
    import capo_wafv2.types.statement

    out["Statement"] = capo_wafv2.types.statement.serialize_aws_json_1_1(
        value["statement"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotStatement:
    out: NotStatement = {}  # type: ignore[typeddict-item]
    if "Statement" in data:
        import capo_wafv2.types.statement

        out["statement"] = capo_wafv2.types.statement.deserialize_aws_json_1_1(
            data["Statement"]
        )
    else:
        raise DeserializationError("NotStatement.statement required")
    return out
