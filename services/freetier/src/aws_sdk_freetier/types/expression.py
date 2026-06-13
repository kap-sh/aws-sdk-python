"""Generated from Smithy shape ``com.amazonaws.freetier#Expression``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_freetier.types.dimension_values
    import aws_sdk_freetier.types.expression
    import aws_sdk_freetier.types.expressions

Expression = TypedDict(
    "Expression",
    {
        "or": NotRequired["aws_sdk_freetier.types.expressions.Expressions"],
        "and": NotRequired["aws_sdk_freetier.types.expressions.Expressions"],
        "not": NotRequired["aws_sdk_freetier.types.expression.Expression"],
        "dimensions": NotRequired[
            "aws_sdk_freetier.types.dimension_values.DimensionValues"
        ],
    },
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Expression) -> dict:
    out: dict = {}
    if "or" in value:
        import aws_sdk_freetier.types.expressions

        out["Or"] = aws_sdk_freetier.types.expressions.serialize_aws_json_1_0(
            value["or"]
        )
    if "and" in value:
        import aws_sdk_freetier.types.expressions

        out["And"] = aws_sdk_freetier.types.expressions.serialize_aws_json_1_0(
            value["and"]
        )
    if "not" in value:
        import aws_sdk_freetier.types.expression

        out["Not"] = aws_sdk_freetier.types.expression.serialize_aws_json_1_0(
            value["not"]
        )
    if "dimensions" in value:
        import aws_sdk_freetier.types.dimension_values

        out["Dimensions"] = (
            aws_sdk_freetier.types.dimension_values.serialize_aws_json_1_0(
                value["dimensions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if "Or" in data:
        import aws_sdk_freetier.types.expressions

        out["or"] = aws_sdk_freetier.types.expressions.deserialize_aws_json_1_0(
            data["Or"]
        )
    if "And" in data:
        import aws_sdk_freetier.types.expressions

        out["and"] = aws_sdk_freetier.types.expressions.deserialize_aws_json_1_0(
            data["And"]
        )
    if "Not" in data:
        import aws_sdk_freetier.types.expression

        out["not"] = aws_sdk_freetier.types.expression.deserialize_aws_json_1_0(
            data["Not"]
        )
    if "Dimensions" in data:
        import aws_sdk_freetier.types.dimension_values

        out["dimensions"] = (
            aws_sdk_freetier.types.dimension_values.deserialize_aws_json_1_0(
                data["Dimensions"]
            )
        )
    return out
