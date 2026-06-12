"""Generated from Smithy shape ``com.amazonaws.wafregional#SqlInjectionMatchSetUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_action
    import aws_sdk_waf_regional.types.sql_injection_match_tuple


class SqlInjectionMatchSetUpdate(TypedDict):
    action: "aws_sdk_waf_regional.types.change_action.ChangeAction"
    """<p>Specify <code>INSERT</code> to add a <a>SqlInjectionMatchSetUpdate</a> to a <a>SqlInjectionMatchSet</a>. Use <code>DELETE</code> to remove a <code>SqlInjectionMatchSetUpdate</code> from a <code>SqlInjectionMatchSet</code>.</p>"""
    sql_injection_match_tuple: (
        "aws_sdk_waf_regional.types.sql_injection_match_tuple.SqlInjectionMatchTuple"
    )
    """<p>Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlInjectionMatchSetUpdate) -> dict:
    out: dict = {}
    import aws_sdk_waf_regional.types.change_action

    out["Action"] = aws_sdk_waf_regional.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    import aws_sdk_waf_regional.types.sql_injection_match_tuple

    out["SqlInjectionMatchTuple"] = (
        aws_sdk_waf_regional.types.sql_injection_match_tuple.serialize_aws_json_1_1(
            value["sql_injection_match_tuple"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlInjectionMatchSetUpdate:
    out: SqlInjectionMatchSetUpdate = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_waf_regional.types.change_action

        out["action"] = (
            aws_sdk_waf_regional.types.change_action.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("SqlInjectionMatchSetUpdate.action required")
    if "SqlInjectionMatchTuple" in data:
        import aws_sdk_waf_regional.types.sql_injection_match_tuple

        out["sql_injection_match_tuple"] = (
            aws_sdk_waf_regional.types.sql_injection_match_tuple.deserialize_aws_json_1_1(
                data["SqlInjectionMatchTuple"]
            )
        )
    else:
        raise DeserializationError(
            "SqlInjectionMatchSetUpdate.sql_injection_match_tuple required"
        )
    return out
