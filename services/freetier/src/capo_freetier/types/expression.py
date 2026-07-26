"""Generated from Smithy shape ``com.amazonaws.freetier#Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.dimension_values
    import capo_freetier.types.expression
    import capo_freetier.types.expressions

Expression = TypedDict(
    "Expression",
    {
        "or": NotRequired["capo_freetier.types.expressions.Expressions"],
        "and": NotRequired["capo_freetier.types.expressions.Expressions"],
        "not": NotRequired["capo_freetier.types.expression.Expression"],
        "dimensions": NotRequired[
            "capo_freetier.types.dimension_values.DimensionValues"
        ],
    },
    closed=True,
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Expression) -> dict:
    out: dict = {}
    if "or" in value:
        import capo_freetier.types.expressions

        out["Or"] = capo_freetier.types.expressions.serialize_aws_json_1_0(value["or"])
    if "and" in value:
        import capo_freetier.types.expressions

        out["And"] = capo_freetier.types.expressions.serialize_aws_json_1_0(
            value["and"]
        )
    if "not" in value:
        import capo_freetier.types.expression

        out["Not"] = capo_freetier.types.expression.serialize_aws_json_1_0(value["not"])
    if "dimensions" in value:
        import capo_freetier.types.dimension_values

        out["Dimensions"] = capo_freetier.types.dimension_values.serialize_aws_json_1_0(
            value["dimensions"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if "Or" in data:
        import capo_freetier.types.expressions

        out["or"] = capo_freetier.types.expressions.deserialize_aws_json_1_0(data["Or"])
    if "And" in data:
        import capo_freetier.types.expressions

        out["and"] = capo_freetier.types.expressions.deserialize_aws_json_1_0(
            data["And"]
        )
    if "Not" in data:
        import capo_freetier.types.expression

        out["not"] = capo_freetier.types.expression.deserialize_aws_json_1_0(
            data["Not"]
        )
    if "Dimensions" in data:
        import capo_freetier.types.dimension_values

        out["dimensions"] = (
            capo_freetier.types.dimension_values.deserialize_aws_json_1_0(
                data["Dimensions"]
            )
        )
    return out
