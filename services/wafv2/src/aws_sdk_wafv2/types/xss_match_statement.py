"""Generated from Smithy shape ``com.amazonaws.wafv2#XssMatchStatement``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.field_to_match
    import aws_sdk_wafv2.types.text_transformations


class XssMatchStatement(TypedDict):
    field_to_match: "aws_sdk_wafv2.types.field_to_match.FieldToMatch"
    """<p>The part of the web request that you want WAF to inspect. </p>"""
    text_transformations: "aws_sdk_wafv2.types.text_transformations.TextTransformations"
    """<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the <code>FieldToMatch</code> request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XssMatchStatement) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.field_to_match

    out["FieldToMatch"] = aws_sdk_wafv2.types.field_to_match.serialize_aws_json_1_1(
        value["field_to_match"]
    )
    import aws_sdk_wafv2.types.text_transformations

    out["TextTransformations"] = (
        aws_sdk_wafv2.types.text_transformations.serialize_aws_json_1_1(
            value["text_transformations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> XssMatchStatement:
    out: XssMatchStatement = {}  # type: ignore[typeddict-item]
    if "FieldToMatch" in data:
        import aws_sdk_wafv2.types.field_to_match

        out["field_to_match"] = (
            aws_sdk_wafv2.types.field_to_match.deserialize_aws_json_1_1(
                data["FieldToMatch"]
            )
        )
    else:
        raise DeserializationError("XssMatchStatement.field_to_match required")
    if "TextTransformations" in data:
        import aws_sdk_wafv2.types.text_transformations

        out["text_transformations"] = (
            aws_sdk_wafv2.types.text_transformations.deserialize_aws_json_1_1(
                data["TextTransformations"]
            )
        )
    else:
        raise DeserializationError("XssMatchStatement.text_transformations required")
    return out
