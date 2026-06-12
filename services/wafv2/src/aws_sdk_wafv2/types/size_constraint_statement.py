"""Generated from Smithy shape ``com.amazonaws.wafv2#SizeConstraintStatement``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.comparison_operator
    import aws_sdk_wafv2.types.field_to_match
    import aws_sdk_wafv2.types.size
    import aws_sdk_wafv2.types.text_transformations


class SizeConstraintStatement(TypedDict):
    field_to_match: "aws_sdk_wafv2.types.field_to_match.FieldToMatch"
    """<p>The part of the web request that you want WAF to inspect. </p>"""
    comparison_operator: "aws_sdk_wafv2.types.comparison_operator.ComparisonOperator"
    """<p>The operator to use to compare the request part to the size setting. </p>"""
    size: "aws_sdk_wafv2.types.size.Size"
    """<p>The size, in byte, to compare to the request part, after any transformations.</p>"""
    text_transformations: "aws_sdk_wafv2.types.text_transformations.TextTransformations"
    """<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the <code>FieldToMatch</code> request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraintStatement) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.field_to_match

    out["FieldToMatch"] = aws_sdk_wafv2.types.field_to_match.serialize_aws_json_1_1(
        value["field_to_match"]
    )
    import aws_sdk_wafv2.types.comparison_operator

    out["ComparisonOperator"] = (
        aws_sdk_wafv2.types.comparison_operator.serialize_aws_json_1_1(
            value["comparison_operator"]
        )
    )
    out["Size"] = value.get("size", 0)
    import aws_sdk_wafv2.types.text_transformations

    out["TextTransformations"] = (
        aws_sdk_wafv2.types.text_transformations.serialize_aws_json_1_1(
            value["text_transformations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SizeConstraintStatement:
    out: SizeConstraintStatement = {}  # type: ignore[typeddict-item]
    if "FieldToMatch" in data:
        import aws_sdk_wafv2.types.field_to_match

        out["field_to_match"] = (
            aws_sdk_wafv2.types.field_to_match.deserialize_aws_json_1_1(
                data["FieldToMatch"]
            )
        )
    else:
        raise DeserializationError("SizeConstraintStatement.field_to_match required")
    if "ComparisonOperator" in data:
        import aws_sdk_wafv2.types.comparison_operator

        out["comparison_operator"] = (
            aws_sdk_wafv2.types.comparison_operator.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    else:
        raise DeserializationError(
            "SizeConstraintStatement.comparison_operator required"
        )
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if "TextTransformations" in data:
        import aws_sdk_wafv2.types.text_transformations

        out["text_transformations"] = (
            aws_sdk_wafv2.types.text_transformations.deserialize_aws_json_1_1(
                data["TextTransformations"]
            )
        )
    else:
        raise DeserializationError(
            "SizeConstraintStatement.text_transformations required"
        )
    return out
