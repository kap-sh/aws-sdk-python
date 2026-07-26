"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateSqlInjectionMatchSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.sql_injection_match_set


class CreateSqlInjectionMatchSetResponse(TypedDict, closed=True):
    sql_injection_match_set: NotRequired[
        "capo_waf_regional.types.sql_injection_match_set.SqlInjectionMatchSet"
    ]
    """<p>A <a>SqlInjectionMatchSet</a>.</p>"""
    change_token: NotRequired["capo_waf_regional.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateSqlInjectionMatchSet</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSqlInjectionMatchSetResponse) -> dict:
    out: dict = {}
    if "sql_injection_match_set" in value:
        import capo_waf_regional.types.sql_injection_match_set

        out["SqlInjectionMatchSet"] = (
            capo_waf_regional.types.sql_injection_match_set.serialize_aws_json_1_1(
                value["sql_injection_match_set"]
            )
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSqlInjectionMatchSetResponse:
    out: CreateSqlInjectionMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "SqlInjectionMatchSet" in data:
        import capo_waf_regional.types.sql_injection_match_set

        out["sql_injection_match_set"] = (
            capo_waf_regional.types.sql_injection_match_set.deserialize_aws_json_1_1(
                data["SqlInjectionMatchSet"]
            )
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
