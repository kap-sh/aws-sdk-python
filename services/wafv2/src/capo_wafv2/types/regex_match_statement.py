"""Generated from Smithy shape ``com.amazonaws.wafv2#RegexMatchStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.field_to_match
    import capo_wafv2.types.regex_pattern_string
    import capo_wafv2.types.text_transformations


class RegexMatchStatement(TypedDict, closed=True):
    regex_string: "capo_wafv2.types.regex_pattern_string.RegexPatternString"
    """<p>The string representing the regular expression.</p>"""
    field_to_match: "capo_wafv2.types.field_to_match.FieldToMatch"
    """<p>The part of the web request that you want WAF to inspect. </p>"""
    text_transformations: "capo_wafv2.types.text_transformations.TextTransformations"
    """<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the <code>FieldToMatch</code> request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchStatement) -> dict:
    out: dict = {}
    out["RegexString"] = value["regex_string"]
    import capo_wafv2.types.field_to_match

    out["FieldToMatch"] = capo_wafv2.types.field_to_match.serialize_aws_json_1_1(
        value["field_to_match"]
    )
    import capo_wafv2.types.text_transformations

    out["TextTransformations"] = (
        capo_wafv2.types.text_transformations.serialize_aws_json_1_1(
            value["text_transformations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexMatchStatement:
    out: RegexMatchStatement = {}  # type: ignore[typeddict-item]
    if "RegexString" in data:
        out["regex_string"] = data["RegexString"]
    else:
        raise DeserializationError("RegexMatchStatement.regex_string required")
    if "FieldToMatch" in data:
        import capo_wafv2.types.field_to_match

        out["field_to_match"] = (
            capo_wafv2.types.field_to_match.deserialize_aws_json_1_1(
                data["FieldToMatch"]
            )
        )
    else:
        raise DeserializationError("RegexMatchStatement.field_to_match required")
    if "TextTransformations" in data:
        import capo_wafv2.types.text_transformations

        out["text_transformations"] = (
            capo_wafv2.types.text_transformations.deserialize_aws_json_1_1(
                data["TextTransformations"]
            )
        )
    else:
        raise DeserializationError("RegexMatchStatement.text_transformations required")
    return out
