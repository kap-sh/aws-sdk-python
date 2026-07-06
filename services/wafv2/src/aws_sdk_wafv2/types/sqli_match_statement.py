"""Generated from Smithy shape ``com.amazonaws.wafv2#SqliMatchStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.field_to_match
    import aws_sdk_wafv2.types.sensitivity_level
    import aws_sdk_wafv2.types.text_transformations


class SqliMatchStatement(TypedDict, closed=True):
    field_to_match: "aws_sdk_wafv2.types.field_to_match.FieldToMatch"
    """<p>The part of the web request that you want WAF to inspect. </p>"""
    text_transformations: "aws_sdk_wafv2.types.text_transformations.TextTransformations"
    """<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the <code>FieldToMatch</code> request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents. </p>"""
    sensitivity_level: NotRequired[
        "aws_sdk_wafv2.types.sensitivity_level.SensitivityLevel"
    ]
    r"""<p>The sensitivity that you want WAF to use to inspect for SQL injection attacks. </p> <p> <code>HIGH</code> detects more attacks, but might generate more false positives, especially if your web requests frequently contain unusual strings. For information about identifying and mitigating false positives, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html\">Testing and tuning</a> in the <i>WAF Developer Guide</i>.</p> <p> <code>LOW</code> is generally a better choice for resources that already have other protections against SQL injection attacks or that have a low tolerance for false positives. </p> <p>Default: <code>LOW</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqliMatchStatement) -> dict:
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
    if "sensitivity_level" in value:
        import aws_sdk_wafv2.types.sensitivity_level

        out["SensitivityLevel"] = (
            aws_sdk_wafv2.types.sensitivity_level.serialize_aws_json_1_1(
                value["sensitivity_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqliMatchStatement:
    out: SqliMatchStatement = {}  # type: ignore[typeddict-item]
    if "FieldToMatch" in data:
        import aws_sdk_wafv2.types.field_to_match

        out["field_to_match"] = (
            aws_sdk_wafv2.types.field_to_match.deserialize_aws_json_1_1(
                data["FieldToMatch"]
            )
        )
    else:
        raise DeserializationError("SqliMatchStatement.field_to_match required")
    if "TextTransformations" in data:
        import aws_sdk_wafv2.types.text_transformations

        out["text_transformations"] = (
            aws_sdk_wafv2.types.text_transformations.deserialize_aws_json_1_1(
                data["TextTransformations"]
            )
        )
    else:
        raise DeserializationError("SqliMatchStatement.text_transformations required")
    if "SensitivityLevel" in data:
        import aws_sdk_wafv2.types.sensitivity_level

        out["sensitivity_level"] = (
            aws_sdk_wafv2.types.sensitivity_level.deserialize_aws_json_1_1(
                data["SensitivityLevel"]
            )
        )
    return out
