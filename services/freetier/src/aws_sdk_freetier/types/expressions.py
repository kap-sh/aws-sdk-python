"""Generated from Smithy shape ``com.amazonaws.freetier#Expressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_freetier.types.expression

Expressions: TypeAlias = list["aws_sdk_freetier.types.expression.Expression"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Expressions) -> list:
    import aws_sdk_freetier.types.expression

    out: list = []
    for item in value:
        out.append(aws_sdk_freetier.types.expression.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Expressions:
    import aws_sdk_freetier.types.expression

    out: Expressions = []
    for item in data:
        out.append(aws_sdk_freetier.types.expression.deserialize_aws_json_1_0(item))
    return out
