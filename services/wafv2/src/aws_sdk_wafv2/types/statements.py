"""Generated from Smithy shape ``com.amazonaws.wafv2#Statements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.statement

Statements: TypeAlias = list["aws_sdk_wafv2.types.statement.Statement"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Statements) -> list:
    import aws_sdk_wafv2.types.statement

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.statement.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Statements:
    import aws_sdk_wafv2.types.statement

    out: Statements = []
    for item in data:
        out.append(aws_sdk_wafv2.types.statement.deserialize_aws_json_1_1(item))
    return out
